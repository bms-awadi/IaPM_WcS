with source as (

    select * from {{ source('dbt_quest', 'raw_orders') }}

),

renamed as (

    select
        id as order_id,
        customer as customer_id,
        ordered_at,
        store_id
    from source

)

select * from renamed
