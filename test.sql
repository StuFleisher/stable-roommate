select student1_id, student2_id, count(student2_id)
from pairs
where student1_id=karly
order by count(student2_id) desc


[{student1_id:karly, student2_id:stuart, count:3},...]