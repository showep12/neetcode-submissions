-- Write your query below
-- select 
--   from customers cus
--   inner join orders ord
--         on cus.customer_id = ord.customer_id
--  where        

--  ;

select cus.customer_id, cus.customer_name
  from customers cus
  inner join 
    (
    select customer_id
    from orders   
    group by customer_id 
    having sum(case when product_name in ('A') then 1 else 0 end) > 0
        and sum(case when product_name in ('B') then 1 else 0 end) > 0
        and sum(case when product_name in ('C') then 1 else 0 end) = 0
    ) ord
    on ord.customer_id = cus.customer_id
    order by cus.customer_name asc