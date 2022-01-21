import binarysearchtree
import linkedlist
import math
import random
import time
import decimal
'''
For this part, I find sometimes n = 10 searches faster than n = 5. So the
linear plot will have a negative value of slope; which I think is normal;
when encountering this circumstance, please rerun the program to insure that
the total search time of n = 10 is larger than that of n = 5;
relatively larger value of NUMBER_OF_TREES will lead to better simulation
compared to those with smaller NUMBER_OF_TREES value.
'''

NUMBER_OF_TREES = 100000


def random_tree(n):
    binary_search_tree = binarysearchtree.BinarySearchTree()
    linked_list = linkedlist.LinkedList()
    for i in range(n):
        random_intenger = random.randint(1,1000)
        binary_search_tree.insert(random_intenger)
        linked_list.insert(random_intenger)
    return binary_search_tree,linked_list


# Due to the fact that all the value computed through search operation is
# quite small, I try to use decimal.Decimal() to increase its precision.
if __name__ == '__main__':
    X =[i for i in range(5,105,5)]
    Y = []
    Y4 = []
    for current_n in X:
        total_time = 0
        total_time2 = 0
        for i in range(NUMBER_OF_TREES):
            binary_search_tree,linked_list = random_tree(current_n)

            time_begin = time.time()
            result = binary_search_tree.search(42)
            time_end = time.time()
            time_ = decimal.Decimal(time_end) - decimal.Decimal(time_begin)
            total_time =decimal.Decimal(total_time) +decimal.Decimal(time_)

            time_begin2 = time.time()
            result2 = linked_list.search(42)
            time_end2 = time.time()
            time_2 = decimal.Decimal(time_end2) - decimal.Decimal(time_begin2)
            total_time2 =decimal.Decimal(total_time2) +decimal.Decimal(time_2)
        # print(total_time)
        average_time = decimal.Decimal(total_time) / decimal.Decimal(NUMBER_OF_TREES)
        Y.append(average_time)
        average_time2 = decimal.Decimal(total_time2) / decimal.Decimal(NUMBER_OF_TREES)
        Y4.append(average_time2)

    # print(Y)
    c = decimal.Decimal((decimal.Decimal(Y[1])-decimal.Decimal(Y[0])))/decimal.Decimal((10-5))
    b = decimal.Decimal(Y[1]) - decimal.Decimal(10*c)
    Y2 =[c*n+b for n in X]

    log_x = [math.log2(i) for i in X]
    c1 = decimal.Decimal((decimal.Decimal(Y[1])-decimal.Decimal(Y[0])))/decimal.Decimal((log_x[1]-log_x[0]))
    b1 = decimal.Decimal(Y[1]) - decimal.Decimal(log_x[1])*decimal.Decimal(c1)
    Y3 = [c1*decimal.Decimal(q)+b1 for q in log_x]


    import matplotlib.pyplot as plt
    plt.plot(X, Y)
    plt.plot(X, Y2)
    plt.plot(X, Y3)
    plt.plot(X,Y4)
    plt.legend(["BST","linear","Logarithmic","LL"])
    plt.xlabel('Size of trees')
    plt.ylabel('Search time')
    plt.ticklabel_format(axis='both', style='sci',scilimits=(0,0))
    plt.show()

'''
Complexity analysis X vs Y:
In the best case scenario, the search operation in a BST structure takes 1 time, 
so the time complexity in best case scenario can be described as O(1).

When adding random values into BST, this structure will become reasonably "bushy", 
so every time you finish a search operation, you halve the work load. In this case,
the best case scenario of the time complexity is still O(1), But in the worst case scenario, 
the result improves a lot to O(log(n)), where n is the total number of values stored in the structure
and the real time complexity will be somewhere between them.

However, when adding sequence into a BST structure in order, the BST will grow "spindly" and degenerate into
a Linked List structure, in this case, the time complexity will range from O(1) to O(n) depending
on the relative size of the target. In this case, the real search time complexity will be somewhere between O(1)
and O(n)

To avoid a tree grown spindly, in my course work, I try to balance the BST by conducting
certain rotation, and I find the NUMBER_OF_TREES used to calculate average time of search
operation have impact on the final result, so I tried several values from 1000 to 100000;
clearly, the relationship between X and Y is logarithmic. For a larger NUMBER_OF_TREES,
this relationship will be much more clear.

'''


"""

Complexity analysis X vs Y, Y2 and Y3
In my course work, because I have balanced my Binary Search Tree, so my
Y followed Y3 reasonably good, especially when having a large NUMBER_OF_TREES
and TREE_SIZE value. In most cases, my Y is lower than Y3, since in most time, I don't have
to search all the way down to the bottom of the structure to fetch 42.
In a normal BST, due to the risk of getting a spindly grown tree, the search time cold be proximity
to linear time and larger than logarithmic. 
To fix it so that Y gets closer to an ideal complexity I think there are at least two ways. 
First, we can disrupt the order of input to get a bushy tree. 
Second, we can do a little bit extra work to ensure every time we insert and delete from a tree,
the structure is still balanced just like what I have done in the coursework.

"""

"""
Complexity analysis X vs Y, Y2, Y3 and Y4
Clearly, from the graph, BST structure's slope is lower than linked list's, which means
 BSTs perform way much better than linked lists, since linked list
takes linear time and BST, especially Balanced BST, takes logarithmic time.

"""