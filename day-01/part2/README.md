# Day 01

## Part 2

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a **three-measurement sliding window**. Again considering the above example:

>199  A  
200  A B  
208  A B C  
210  &nbsp; &nbsp; B C D  
200  E &nbsp; &nbsp; C D  
207  E F &nbsp; &nbsp; D  
240  E F G  
269  &nbsp; &nbsp; F G H  
260  &nbsp; &nbsp; &nbsp; &nbsp; G H  
263  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; H
>

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked `A (199, 200, 208);` their sum is `199 + 200 + 208 = 607`. The second window is marked `B (200, 208, 210);` its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison **increased**.

Your goal now is to count **the number of times the sum of measurements in this sliding window increases** from the previous sum. So, compare `A` with `B`, then compare `B` with `C`, then `C` with `D`, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

>A: 607 (N/A - no previous sum)  
B: 618 (**increased**)  
C: 618 (no change)  
D: 617 (decreased)  
E: 647 (**increased**)  
F: 716 (**increased**)  
G: 769 (**increased**)  
H: 792 (**increased**)  

In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. **How many sums are larger than the previous sum?**
