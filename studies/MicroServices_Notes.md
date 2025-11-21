# Distribution
> a distributed system is an ensemble of independent computing nodes, that appear as a single execution platform to application running on it. Nodes coordinate transparently with regard to the application. Distribution requires concurrency and scalability. It's opposite is centralization

# Concurrency
> Distribution entails complex concurrent work in individual nodes, as the application runs on them, and across the nodes to propagate the effects of the execution. Efficient organization needs concurrency, efficient communications need advanced network protocols.



 HOW CONCURRENCY EXPRESSED IN A PROGRAMMING LANGUAGE

**System-level**: concurrency in a programming languages can be provided binding keywords to underlying OS fork and exec syscalls. The language expression and semantic are taken outside the language

**Language-level**: an alternative is to accommodate multiple control points in a language. THe runtime virtualizes them using the processor's single program counter. This involves abstracting threads within the program's process, essentially creating a multithreaded program that runs on a OS supporting multi-programming
    - Language-level concurrency offers benefit such as improved readability and portability of program along with expressive and efficient concurrency models. However it comes with the cost of independence form the underlying operating system and potential loss of generality due to the predefined concurrency model.



Model of concurrency:

1. Concurrent entities
   1. *active*: able to execute without depending on the commend of other
   2. *reactive*: only capable of executing in response to the command of other
   3. *resources*: with an internal state, and pre-and-post conditions applying on access to it
   4. *passive*: with no internal state, like a plain procedure
2. Concurrency abstraction: a model require three distinct concurrency abstraction
   1. A threads: to represent active entities
   2. active-control resources: for example threaded servers, they use sophisticated access protocols but they are heavier they cost like a thread even if quiescent
   3. passive control resources: with semaphore as monitor they are less expressive algorithmically than threads and they are lighter without a scheduling to execute








