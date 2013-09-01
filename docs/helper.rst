Section Header
==============

**emphasis (bold/strong)**

*italics*

Simple link: http://django.2scoops.org
Fancier link: `Django`

.. _`Django`: http//django.2scoops.org

Subsection Header
-----------------

#) An enumerated list item

#) Second item

* First bullet

* Second bullet

	* Indented Bullet
	* Note carriage return and idents

Literal code block::

	def like:
		print("I like ice cream")

	for i in range(10):
		like()

Python colored code block (requires pygments):

code-block:: python

	# You need to "pip install pygments" to make this work.

	for i in range(10):
		like()

Javascript colored code block:


code-block:: javascript
	
	conse.log("Don't use alert()");
	