Mutex-Based Solution:

By using a mutex (table_lock) to protect the critical section where forks are picked up, we ensure that only one philosopher can pick up forks at a time, preventing deadlock.
This approach introduces fairness and avoids starvation as all philosophers get an equal chance to access the forks.

Explanation of the Five Dining Philosophers Problem
The Dining Philosophers problem is a classic synchronization problem proposed by Edsger Dijkstra. It involves five philosophers who sit around a circular table. Each philosopher alternates between thinking and eating. There are five forks placed between the philosophers, and a philosopher needs both the fork on their left and the fork on their right to eat.

Potential Issues
Deadlock:

A deadlock can occur if each philosopher picks up the fork on their left simultaneously and then waits indefinitely for the fork on their right.
In this scenario, all philosophers end up holding one fork and waiting for the other, resulting in a cycle of dependencies with no one able to proceed.
Starvation:

Starvation can occur if a particular philosopher is unable to access both forks for an extended period due to other philosophers constantly picking up the forks before them.
This situation can lead to some philosophers eating frequently while others might starve.
