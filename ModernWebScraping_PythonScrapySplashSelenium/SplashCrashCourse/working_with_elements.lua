function main(splash, args)
    
    --splash:set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15")
    
    --[[
    headers = {
        ['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'
    }
    splash:set_custom_headers(headers)
    --]]
    
    splash:on_request(function(request)
        request:set_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15')
    end)

	url = args.url
  assert(splash:go(url))
  assert(splash:wait(1))
  
  input_box = assert(splash:select("#search_form_input_homepage"))
	input_box:focus()
  input_box:send_text("my user agent")
  assert(splash:wait(0.5))
  
  --[[
  search_button = assert(splash:select("#search_button_homepage"))
  search_button:mouse_click()
  assert(splash:wait(5))
  --]]
  
  input_box:send_keys("<Enter>")
  assert(splash:wait(5))
  
  splash:set_viewport_full()
  
  return {
    image = splash:png(),
    html = splash:html()
  }
endd