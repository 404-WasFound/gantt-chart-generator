# Gantt Chart Generator
A text-based gantt chart generator written in python

## Overview

### .mkpf Files
```
#start header_name
-item_name ; 1-8
#end header_name
```
**Understanding the sytax**

Opens the header
```
#start header_name
```
- `#start`: Starts header
- `header_name`: Name of the header

Creates an item
```
-item_name ; 1-8
```
- `-`: Creates item
- `item_names`: Names of the item
- ` ; `: Splits the item name and the item date / days
- `1-8`: Days (from 1 - maximum dates), these will be displayed as their respectives dates
