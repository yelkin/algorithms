#include <stdio.h>
#include <stdlib.h>

typedef struct list {
    int data;
    struct list* next;
} list_t;

list_t* reverse(list_t* list) {
    list_t *p=list, *q=NULL, *r;

    while(p != NULL) {
        r = q;
        q = p;
        p = p->next;
        q->next = r;
    }
    return q;
}

void print(list_t* list) {
    while(list != NULL) {
        printf("%d ", list->data);
        list = list->next;
    }
    printf("\n");
}

list_t* new_list(int size, int *data) {
    if (size < 1) return NULL;

    list_t* head = malloc(sizeof(list_t));
    head->data = data[0];
    head->next = NULL;

    list_t* cur = head;
    int i;

    for(i=1; i<size; i=i+1) {
        cur->next = malloc(sizeof(list_t));
        cur = cur->next;
        cur->data = data[i];
        cur->next = NULL;
    }
    return head;
}

int main(int argc, char**argv) {
    if(argc < 2) {
        printf("Usage: a.out 1 2 3 ...\n");
        return 0;
    }
    int size = argc-1;
    int data[size];
    int i;
    for(i=0; i < size; i = i + 1) {
        data[i] = atoi(argv[i+1]);
    }
    list_t* list = new_list(size, data);
    list = reverse(list);
    print(list);
    return 0;
}
