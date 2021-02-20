# json-pasing

### Navigates user through the given .json file.

#### Explanation
- If user enters a key, he/she will get its value.
- If the value of the given key is also an object, then object's keys will be displayed to the user and he/she will be able to choose one out of them
- If the value of the given key is a list, then its length will be displayed and the user will be able to enter the index of list's item that he/she wants to get.<br>
**NOTE: the indexing of the list starts from 1**

#### Example
```
Here are the keys of the dictionary, enter the key to get its value. Keys:
['users',
 'next_cursor',
  ...]
Enter the key: users

The object is a list, please enter the id of the element you want to get.
 Length of the list: 1
NOTE! THE INDEXING STARTS FROM 1
Enter the list id: 1
Here are the keys of the dictionary, enter the key to get its value. Keys:
['id',
  ...]
Enter the key: id
1330457336
```