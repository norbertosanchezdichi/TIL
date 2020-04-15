function main(splash, args)
	url = args.url
  assert(splash:go(url))
  assert(splash:wait(1))
  
  input_box = assert(splash:select("#search_form_input_homepage"))
	input_box:focus()
  input_box:send_text("my user agent")
  assert(splash:wait(0.5))
  
  search_button = assert(splash:select("#search_button_homepage"))
  search_button:mouse_click()
  assert(splash:wait(5))
  
  return {
    image = splash:png(),
    html = splash:html()
  }
end