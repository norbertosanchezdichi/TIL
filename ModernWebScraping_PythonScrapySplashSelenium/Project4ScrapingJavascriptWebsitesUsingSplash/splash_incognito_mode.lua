function main(splash, args)
  url = args.url
  assert(splash:go(url))
	assert(splash:wait(1))
  
  rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
	rur_tab[3]:mouse_click()
  assert(splash:wait(1))
	splash:set_viewport_full()
  
  return splash:png()

end