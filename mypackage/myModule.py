def top_n(items, n):
    '''Return the top n items in an array, in descending order.

    Args:
        items(array): list or array-like object
        n (int): num of items to return

    Return:
        array: top n items, in descending order

    Egs:
        >>> top_n([8,3,2,7,4], 3)
            [8,7,3]

            explanation, we passed a list or array in the argument
            and said we want the top 3 as n = 3 then it returns an array or 
            list like object consisting of 3 elements in descencding order

    '''       
    for i in range(n):  # keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # if this item is bigger than next item..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!

    # get last two items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]