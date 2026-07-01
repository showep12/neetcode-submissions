-- Write your query below
select cus.name
  from customers cus
  left outer join orders ord
               on cus.id = ord.customer_id
where ord.id is null 
