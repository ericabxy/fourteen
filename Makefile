BUILD = ./extractPve

normal: html/TestChar.html
	$(MAKE) TestChar.xml

%.xml: html/%.html
	$(BUILD) $< > docs/$@
