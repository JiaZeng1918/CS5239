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

1.  YouTube handles uploads of multiple hundreds of hours of video every minute
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







##  SYSTEM DESIGN System design





## Deployment at scale



##  Conclusion

