$('#main-product').click(function () {
  console.log('aria clicked')
  let checkbox_list = $('.checkbox-category:checked').toArray()
  console.log(checkbox_list)
  let new_link = '?'

  if (checkbox_list.length > 0){
      console.log(checkbox_list[0].id)
      let list_of_ids = checkbox_list.map(el => el.id.replace('product', 'product='))
      console.log(list_of_ids)
      console.log(list_of_ids.join('&'))
      new_link = '?' + list_of_ids.join('&')

  }

  $('#product-filter-button').attr('href', new_link)
})
$('.change_merchan_count').click(function () {
  let order_id = $(this).attr('id').slice(8)
  let action = $(this).attr('id').slice(0, 8)
  let button  = $(this).siblings('.order_count')
  console.log(order_id)

  $.ajax({
    url: `/change_order_count/${order_id}`,
    method: 'GET',
    data: {
      'action': action
    },
    success: function (result) {
      if (result.status === 'ok'){
        console.log('ok to action');
        console.log(result.new_number)
        $(button).text(result.new_number)
        update_total()
      }
    }
  })



})


function update_total(){
  let orders = $('.order_row');
  let total_cost = 0;
  for (let order of orders){
    let count = $(order).find('.order_count').text()
    let cost = $(order).find('.order_cost').text()

    total_cost += (+count) * (+cost)
  }
  $('#total_cost').text(total_cost + '$')
}

$('.order_table').click(function () {
  update_total()
})

$(".delete_order").click(function () {
  let slug = $(this).attr('id').slice(6)
  let row = $(this).closest('.order_row')
  console.log(slug)

    $.ajax({
    url: `/delete_from_card/${slug}`,
    method: 'GET',
    success: function (result) {
      if (result.status === 'ok'){
        row.remove()
        update_total()
      }
    }
  })

})


function searchToggle(obj, evt){
    var container = $(obj).closest('.search-wrapper');
        if(!container.hasClass('active')){
            container.addClass('active');
            evt.preventDefault();
        }
        else if(container.hasClass('active') && $(obj).closest('.input-holder').length == 0){
            container.removeClass('active');
            // clear input
            container.find('.search-input').val('');
        }
}