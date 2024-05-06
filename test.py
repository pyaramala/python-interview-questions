import random
import time
names = ['pradeep','kumar','nani','siva']
subject = ['python','java','scala','c++']
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id':i,
            'name':random.choice(names),
            'subject':random.choice(subject)
        }
        result.append(person)
    return result
t1 = time.time()
peoples=people_list(1000000)

t2 = time.time()
print(f"Took: {t2-t1}")

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id':i,
            'name': random.choice(names),
            'subject': random.choice(subject)
        }
        yield person
t1 =time.time()
peoples = people_generator(1000000)

t2 = time.time()
print(f"Took: {t2-t1}")