# Geometric Intuition for Deep Learning

I find machine learning (ML) and deep learning much easier to understand when I think about geometry than equations.  I can gain intuition by reasoning about points and the distances between them, loss-surfaces, manifolds, and hyper-planes.  Here's a collection of resources to understand ML in this way.

## High dimensional spaces

High dimensional spaces often behave in counter-intuitive ways compared to the 2-D or 3-D spaces that we typically engage with.  [Dive in](high-dimensionality/) to some of those differences.


## Explaining ML models

On 21 Aug 2019 i gave a talk on Explaining ML models.  The [explainability](explainability/) directory includes the notebooks I used to generate the charts and equations for this talk.


# Note about python 3

Everything here is written for python 3 only.  If you're still using python 2.7, please _please_ stop.  Python 2.7 is at the end of its life, and will soon not even receive critical security updates.  At this point in time, the year 2019, it is actually irresponsible to write code in python 2.7, because you are enabling people to deploy systems that will not be secure, which could lead to actual real-world harm.  So if the team you're on still hasn't upgraded, take a moment to consider all the bad things that could happen if hackers got into your code and there was literally nothing you could do to stop them except turn off your system or spend weeks or months upgrading to python 3.  So get ahead of that now.  

Plus you get nice things like [type hints](https://docs.python.org/3/library/typing.html) and [f strings](https://realpython.com/python-f-strings/) which make the code easier to read.
