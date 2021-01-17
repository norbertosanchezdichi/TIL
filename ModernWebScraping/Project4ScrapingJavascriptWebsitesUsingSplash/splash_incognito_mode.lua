function main(splash, args)
  
  splash.private_mode_enabled = false
  
  url = args.url
  assert(splash:go(url))
	assert(splash:wait(1))
  
  usd_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
	usd_tab[3]:mouse_click()
  assert(splash:wait(1))
	splash:set_viewport_full()
  
  return splash:html()

end