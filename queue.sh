Que
Que is the collection of ordered elements in which addition and removal of element takes places at different end.
The end where elements are added is called back/rear/tail. The end where elements are removed is called front/head.
stored element in order of FIFO/LILO Methodologies
The process of adding elements to queue is ca,led enqueue and process of removing elemetn is called dequeue
operation:enqueue,dequeue,isfull, isempty
queue are used when we need to process one element at a time.eg callcenterse. egs:printing multiple docs



IN priority que, insertion and removal is done at different end. But removal is based on priority of element.
to set priority, 2 ways:
1-Element itself is considered as priority or elemnt with its priority is added as tuple.
in element as priority, the lowest value highest priority or highest value highest priority can be used as priority.


priority que can be implemented by list or module queue,
if using list, we need to sort list after appending element and need to perform pop(0)
or another way usiing priorityqueue in queue module. Here loewst element is removed first.
