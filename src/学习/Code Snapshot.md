---
layout: post
title: Snapshot
slug: Snapshot
date: 2020-03-11 17：00
status: publish
author: Gary
categories: 
- Code
tags: 
- C/C++
---

交换内容，形参影响实参
```c
#include <stdio.h>
void swap(int *p1,int *p2)
{
    int temp;
    temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}
int main()
{
    int a,b;
    int *p1 = &a,*p2 = &b;
    scanf("%d%d",p1,p1);
    swap(p1,p2);
    printf("%d,%d",*p1,*p2);
}
```

交换地址，形参不影响实参

```c
#include <stdio.h>
void swap(int *p1,int *p2)
{
    int *temp;
    temp = p1;
    p1 = p2;
    p2 = temp;
}
int main()
{
    int a,b;
    int *p1 = &a,*p2 = &b;
    scanf("%d%d",p1,p1);
    swap(p1,p2);
    printf("%d,%d",*p1,*p2);
}
```

出错，temp指针所指地址未初始化，导致出错

```c
#include <stdio.h>
void swap(int *p1,int *p2)
{
    int *temp;
    *temp = *p1;
    *p1 = *p2;
    *p2 = *temp;
}
int main()
{
    int a,b;
    int *p1 = &a,*p2 = &b;
    scanf("%d%d",p1,p1);
    swap(p1,p2);
    printf("%d,%d",*p1,*p2);
}
```

---