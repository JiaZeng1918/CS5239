# Warehouse-Scale Video Acceleration: Co-design and Deployment in the Wild

## 1 Introduction

Video is the dominant form of internet traffic making up >60% of global internet traffic as of 2019, and the demand is growing given new technologies. However, the improvements from Moore's Law have stalled.

#### Prior work

Prior work on video acceleration focused on **consumer** and **end-user systems**, like **mobile devices**, **desktops**, and **televisions**. But little attention to the data center.

#### Requirements

1. High quality
2. Availability
3. Throughput
4. The efficiency of cloud deployments
5. The complexity of server-side video transcoding
6. Deployment at scale
7. Co-design with large-scale distributed systems

#### Contributions

1. Present a new holistic system for video acceleration with a new hardware accelerator building block - *video coding unit* (VCU)
2. Present detailed data and insights from deployment at scale in Google

## 2 Warehouse-Scale video processing

### 2.1 Video Transcoding: Workload challenges

#### A plethora of output files

Video sharing platforms like YouTube:

![image-20221017201607207](C:\Users\Jia\AppData\Roaming\Typora\typora-user-images\image-20221017201607207.png)

YouTube converts source videos to a standard group of 16:9 resolutions (1920:1080, 2560:1440). Then these video files are computed and saved to the cloud storage system. (Differ from video chat)

#### A plethora of video formats

Compressing video files makes them small, which is good for storage and network bandwidth.

Higher compression gains come with more computation.

Some devices support the latest specifications via software decoders (like laptops) and some devices (like tv) do not.

So the videos must be encoded in a plethora of different formats.

A wide range of resolutions and formats translates to a heavy workload in the video processing platform spent on **transcoding**.

#### Algorithmic trade-offs in video transcoding

Transcoding process

![image-20221017205412832](C:\Users\Jia\AppData\Roaming\Typora\typora-user-images\image-20221017205412832.png)

Companies need to optimize these trade-offs to ensure that users receive **playable** and **high-quality** video bitstreams while minimizing their own **computational** and **network costs**.

Encoding is a computationally hard search problem and often takes more time than decoding.

Another key parameter to improve video quality and bitrate: **non-causal information** about the video frame sequence

Choose an algorithm from:

1. one-pass
2. two-pass

Used in different modes:

1. Low-latency
2. Lagged
3. Offline

Example:

1. Low-latency & one-pass: Video conferencing and gaming
2. Low-latency & two-pass: no future information
3. Lagged & two-pass: contains future information and allows for bounded latency (Live stream)
4. Offline & two-pass: The best quality (YouTube and Netflix)

#### Chunking and parallel transcoding modes

Leverage warehouse infrastructure to run as much in parallel as possible.

Two kinds of transcoder methods:

1. Single-output transcoding (SOT)
2. Multiple-output transcoding (MOT)

![image-20221017211927155](C:\Users\Jia\AppData\Roaming\Typora\typora-user-images\image-20221017211927155.png)

MOT is generally preferred to SOT, as it avoids redundant decodes for the same group of outputs, but SOT may be used when memory or latency needs mandate it

### 2.2  Warehouse-Scale Processing: Challenges

#### Multiple video workloads and requirements:

Examples:

1. YouTube handles uploads of multiple hundreds of hours of video every minute
2. Google Photos and Google Drive with a similar volume of videos
3. YouTube Live with hundreds of thousands of concurrent streams

These services differ in load, access patterns, and latency requirements

#### Video usage patterns at scale

Three buckets:

1. Very popular videos
2. Modestly watched videos
3. Long tail

#### Data center requirements

Focuses on

1. cost efficiency,
2. throughput, and
3. scale-out computing
4. "Time to market": deliver significant cost savings at scale
5. Change management: Testing and deploying updates can be highly disruptive in data centers

#### Data center schedulers

Generate an acyclic task dependency graph based on output variants.

Schedule the task to optimize available capacity and concurrency.

## 3 SYSTEM DESIGN System design

#### Globally maximize utilization

#### Optimize for deployment at scale

#### Design for agility and adaptability

### 3.1 Video accelerator holistic systems design

#### Overall design

![image-20221018144833564](C:\Users\Jia\AppData\Roaming\Typora\typora-user-images\image-20221018144833564.png)

Each cluster operates independently and has:

1. A number of VCU machines
2. Non-accelerated machines

VCU ASIC contains:

1. Multiple encoder cores
2. Sufficient decode cores
3. Network-on-chip (NoC)
4. DRAM bandwidth

#### ASIC level

Select parts of transcoding to implement in silicon based on maturity and computational cost.

Candidates:

1. Encoding data path is the most expensive in computing and DRAM bandwidth. Primary candidate
2. Decoding is the next dominant computing cost. Second candidate
3. The rest of the system is left flexible

#### Board and rack levels

Deploy multiple VCUs per host to **amortize overheads** and **avoid standing encoder throughput**

#### Cluster level

Work graph: cluster-wide work queue onto parallel worker nodes (includes both transcoding and non-transcoding steps)

Each VCU worker node runs a process per transcode to constrain errors to a single step.

This scheduler is fundamental to maximizing VCU utilization data center-wide.

The key to maximizing VCU utilization: maximizing the encoder utilization. And the MOT is foundational for encoder utilization.

Method: multiple MOTs and SOTs in parallel are performed to boost encoder and VCU utilization.

### 3.2 VCU encoder core design

Encoder core shares some architecture features with other prior work:

1. Pipelined architecture
2. Local reference store for motion estimation and other state
3. Acceleration of entropy encoding

However, all above is optimized for data center quality, deployment, and  power/performance/area targets

#### Main functional blocks in the pipeline

![image-20221018161837087](C:\Users\Jia\AppData\Roaming\Typora\typora-user-images\image-20221018161837087.png)

The basic element of the pipelined computation:

1. Macroblock (H.264, 16x16)
2. Superblock (VP9, 64x64)

#### Encoder core pipeline stages

1. First stage is the classic stages of a block-based video encoding algorithm: motion estimation, sub-block partitioning, and rate-distortion-based transform and prediction mode selection
2. Second stage: entropy encoding
   1. decoding of the macroblock
   2. temporal filtering for creating of VP9’s alternate reference frames
3. Final stage: loop filtering and lossless frame buffer compression

#### Data flow and memory system

The DRAM reader block:

1. The interface to the NoC subsystem, and is responsible for fulfilling requests for data from other blocks, primarily the reference store
2. Includes the preprocessor and frame buffer decompression logic

The DRAM writer block is the same as DRAM reader block (write to DRAM and interface to the NoC subsystem)

#### Control and stateless operation

The bandwidth overhead from transferring state from DRAM is relatively small compared to the bandwidth needed to load reference frames.

While an embedded encoder (in a camera, for example) might prefer to retain state across frames to simplify processing its single stream, this stateless architecture is better for a data center ASIC where multiple streams of differing resolutions and frame rates (and hence processing duration) are interleaved

### 3.3 System balance and software co-design

#### Provisioning and System Balance

![image-20221022133234808](C:\Users\Jia\AppData\Roaming\Typora\typora-user-images\image-20221022133234808.png)

Each machine has  2 accelerator trays.

Each accelerator tray contains 5 VCU cards.

Each VCU card contains 2 VCUs.

Given  20 VCUs per host

 VCU DRAM bandwidth: Each encoder core can encode 2160p in real-time, up to 60 FPS (frames-per-second) using three reference frames

VCU DRAM capacity

Network bandwidth

#### Co-Design for fungibility and iterative design

Software and hardware: loosely coupled to  facilitate parallel development pre-silicon and continuous iteration post-silicon

The codec cores in the VCU are programmed as opaque memories by the on-chip management firmware.

Userspace command: : run-on-core, copy-from-device-to-host, copy-from-host-to-device, and wait-for-done

Assuming that multiple userspace processes would be needed to reach peak utilization at the VCU level since we use a process-per-transcode model and the VCU is fast enough to handle multiple simultaneous streams.

Schedule: round-robin

Iterate on userspace software in data center is easier than on any lower level software (disruption, reboot)

#### Co-design for work scheduling & resiliency

Scheduler: online multi-dimensional bin-packing scheduler (to realize the maximum per-VCU and data center-wide VCU utilization)

1. ensures that no single VCU becomes completely saturated and no video transcoding task (a step in the dependency graph) becomes resource starved
2. Each cluster has multiple logical "pools" of computing defined by use case (upload, live) and priority (critical, normal, batch)
3. Each pool has its own scheduler and multiple workers of different types (e.g. transcoding, thumbnail extraction, generating search signals, fingerprinting, notifications, etc), some with exclusive access to a VCU and some doing regular CPU based processing
4. Each type of worker defines its own set of named scalar resource dimensions and a capacity for each
5. Use synthetic resources to provide an additional level of control (for example, to limit the amount of software decode to indirectly save PCI Express bandwidth which is otherwise hard to attribute to a specific process)
6. The scheduler is horizontally scaled due to a large number of workers and the need for low latency
7. In the event of an error, the work is rescheduled on another VCU or with software transcoding, leveraging the existing video processing framework retry mechanism

![image-20221022142153444](C:\Users\Jia\AppData\Roaming\Typora\typora-user-images\image-20221022142153444.png)

### 3.4 High-level synthesis for agility

#### High Productivity and Code Maintainability

HLS helps to reduce the code size and save time compared with traditional Verilog approach.

#### Massively Accelerated Verification

The standard software development tool flows helps to make verification. HLS exposed over 99% of the functional bugs during C++ testing, before ever running full VCU RTL simulation

#### Focusing Engineering Effort on High-Value Problems

Skip strenuous verification of the microarchitecture since the HLS flow does not suffer the human errors that ail traditional Verilog designs

#### Design Space Exploration

With our flow, we were able to try numerous architectures and algorithms to find optimal quality-silicon area trade-offs for the numerous design choices in many encoding problems. Saving the budget.

#### Late Feature Flexibility

Benefit to further development: For subsequent chip designs, our design flow will make migration to new silicon process nodes and clock frequency targets effortless.

## 4. Deployment at scale

4.1 quantifies the performance and quality improvement

4.2 - 4.4evaluate in post-deployment tuning and in managing failures

4.5 discuss new workloads and application capabilities enabled by hardware acceleration

### 4.1 Benchmarking Performance & Quality

#### Experimental Setup

benchmark: **vbench**

This public benchmark suite consists of a set of **15 representative videos grouped** across a 3-dimensional space defined by **resolution, frame rate, and entropy**

two baselines: Skylake and 4xNvidia T4

our production: 8xVCU and 20xVCU

In the GPU and accelerator systems, all video transcoding is offloaded to the accelerators, and the host is only running the ffmpeg wrapper, rate control and the respective device drivers

#### Encoding Throughput

Metrics: **Throughput** [Mpix/s] and **perf/TCO** (performance per total cost of ownership)

Offline two-pass single output (SOT) throughput in VCU vs. CPU and GPU systems:

![Table1](img/Table1.png)

Production workload is largely MOT, which was not supported on our GPU baseline.

And MOT throughput is 1.2-1.3x higher than SOT

Results:

* For H.264, the GPU has 3.5x higher throughput, and the 8xVCU and 20xVCU provide 8.4x and 20.9x more throughput
* For VP9, the 20xVCU system has 99.4x the throughput of the CPU baseline.
* the perf/TCO improvement of the VCU system over the baseline is 4.4x with 4 cards, and 7.0x in the denser production system
* In a perf/watt comparison of the systems, the VCU system achieves 6.7x better perf/watt than the CPU baseline 10 for single output H.264, and 68.9x higher perf/watt on multi-output VP9.

#### Encoding Quality

Following Figure shows the operational rate-distortion (**RD**) curves for each vbench video, with peak signal-to-noise ratio (**PSNR**) representing distortion on the vertical axis, **bitrate** (bits per second of video stream) on the horizontal axis.

![Figure7](img/Figure7.png)

RD results:

* H.264 is visible in Figure 7 (higher is better), where the RD curves in the bottom graphs have shifted to the left, i.e. the VP9 encoder uses fewer bits while maintaining comparable visual quality.
* The RD curves also show the high variance in encoding quality across videos. e.g. presentation and desktop vs holi

We compare the encoding quality of VCU using **BD-rate** for each video relative to the software baseline, and average across the suite.

BD-rate represents the average bitrate savings for the same quality (PSNR in this case)

BD-rate results:

* VCU leverages the improved coding efficiency of VP9 relative to H.264 to achieve 30% BD-rate improvement relative to libx264
* VCU H.264 encodings are on average 11.5% higher BD-rate than libx264, and VCU VP9 is 18% greater BD-rate than libvpx.

### 4.2 Production Results

We next present data from fleetwide deployment and tuning, serving real production upload workloads.

Throughput per VCU measured for real production video transcoding workloads

![Figure8](img/Figure8.png)

doing MOT instead of SOT is a big win!!!

### 4.3 Benefits of Co-Design in Deployment

the initial measured throughput of hardware differs from predicted pre-silicon prototyping or simulation/emulation, offering substantial room for improvement post-launch.

Our **co-design** across hardware and software created multiple opportunities for tuning.

Following figure shows **improvement** as the percent difference in **bitrate relative** to software from **the time** the accelerators were deployed.
![Figure10](img/Figure10.png)

Results: Encoder rate control runs exclusively on the host and has improved over time, eventually surpassing software bitrates at iso-quality, including competing with improvements in software encoding.

Following figure show the growth in total throughput per job with chunked output and live transcoding.

One additional benefit of the hardware-software co-design is that the scheduler can make trade-offs to reduce resource stranding.
![Figure9](img/Figure9.png)

### 4.4 Failure Management

Reliability is a first class concern in the full hardware life cycle (delivery, burn-in, fault detection, repair, update, decommission).

#### Failure Monitoring and Workflow

* The VCU firmware provides telemetry from the cards reporting various health and fault metrics (temperature, resets, ECC errors, etc).
* When a sufficient number of faults have accumulated, a host will be marked as unusable and queued for repairs.
* the warehouse scheduler needs to tolerate a modest number of faulty systems in production while human technicians repair those that have been removed.

#### VCU Failures

It is not cost effective to send a system to repair when a small fraction of the VCUs have failed. Accordingly, the failure management system **has the capability to disable an individual VCU** so that the majority of the system can remain available, and the load balancing software adapts to this degradation.

#### Memory/Host Failures

To detect manufacturing escapes, DRAM test patterns are written and evaluated during burnin.

#### Avoiding “Black-Holing”

a failing but not yet disabled VCU is often ‘fast’ relative to a working one and can naturally result in “black-holing”, where a disproportionate amount of traffic is sent to these bad systems.

**Resolution**: a transcoding worker, upon encountering a hardware failure, immediately aborts all work on the VCU, which is retried at the cluster level.

#### Reducing “Blast Radius”

videos are sharded into short chunks and are typically processed in parallel across hundreds of VCUs, so a single failing VCU can corrupt many videos.

**Resolution**: our system includes high-level integrity checks (i.e., video length must match the input) that detect and prevent most corruption. 

### 4.5 New Capabilities Enabled by Acceleration

#### Enabling Otherwise-Infeasible VP9 Compression

Problem: VP9 software encoding is typically 6-8x slower and more expensive than H.264

NEW: in the non-accelerated scenario, VP9 would only be produced for the most popular videos using low-cost batch CPU after upload. With VCUs, we could instead shift to producing both VP9 and H.264 at upload time and leverage efficient MOT encoding.

#### Enabling New Use-Cases

Problem: additional buffering was needed due to high variance in software encoding throughput. This necessarily limited the resolution, quality, and affordability of VP9

NEW: a single VCU can handle this MOT in real time. The consistency of the hardware transcode speed enabled an affordable 5-sec end-to-end latency stream in both H.264 and VP9

## Conclusion
