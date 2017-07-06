pandas
======

.. toctree::
   :maxdepth: 1



DataFrame()
-----------

.. py:class:: DataFrame()
	
	.. code-block:: py

		data = {
			'year': [
				2010, 2011, 2012,
				2010, 2011, 2012,
				2010, 2011, 2012
			],
			'team': [
				'FCBarcelona', 'FCBarcelona', 'FCBarcelona', 
				'RMadrid', 'RMadrid', 'RMadrid',
				'ValenciaCF', 'ValenciaCF', 'ValenciaCF'
			],
			'wins': [
				30, 28, 32, 
				29, 32, 26, 
				21, 17, 19
			],
			'draws': [
				6, 7, 4, 
				5, 4, 7, 
				8, 10, 8
			],
			'losses': [
				2, 3, 2, 
				4, 2, 5, 
				9, 11, 11
			]
		}

		football = pd.DataFrame(
			data , 
			columns = [
				'year', 'team', 'wins', 'draws', 'losses'
			]
		)


read_csv()
----------

.. py:function:: read_csv()

	.. code-block:: py

		edu = pandas.read_csv(
			'some.csv',
			na_values=':',
			usecols=['TIME', 'GEO', 'Value'],
		)

		edu
		"""
		    TIME GEO    Value
	  	0   2000 sg11   sv21
	  	1   2000 sg12   sv22
	  	2   2000 sg13   sv23
	  	...
	  	500 2000 sg1500 sv2500
		"""

		edu.head()
		"""
		  TIME GEO Value
	  	0 2000 sg11 sv21
	  	1 2000 sg12 sv22
	  	2 2000 sg13 sv23
		"""

		edu.tail()
		"""
	  	498 2000 sg1498 sv2498
	  	499 2000 sg1499 sv2499
	  	500 2000 sg1500 sv2500
		"""

		edu.describe()
		"""
		      TIME        Value
		count 384.000000  361.000000
		mean  2005.500000 5.203989
		std   3.456556    1.021694
		min   2000.000000 2.880000
		25%   2002.750000 4.620000
		50%   2005.500000 5.060000
		75%   2008.250000 5.660000
		max   2011.000000 8.810000
		"""

		edu['Value']
		"""
		0 NaN
		1 NaN
		2 5.00
		3 5.03
		4 4.95
		...
		"""

		edu[10:14]
		"""
		   TIME GEO   Value
	  	10 2000 sg110 sv210
	  	11 2000 sg111 sv211
	  	12 2000 sg112 sv212
	  	13 2000 sg113 sv213
	  	14 2000 sg114 sv214
		"""

		edu.ix[90:94 , [’TIME ’,’GEO’]]
		"""
		   TIME GEO   
	  	90 2000 sg190 
	  	91 2000 sg191 
	  	92 2000 sg192 
	  	93 2000 sg193 
	  	94 2000 sg194 
		"""

		edu[edu[’Value ’] > 6.5].tail()
		"""
		    TIME GEO     Value
		218 2002 Cyprus  6.60
		281 2005 Malta   6.58
		94  2010 Belgium 6.58
		93  2009 Belgium 6.57
		95  2011 Belgium 6.55
		"""

		edu[edu["Value"].isnull()].head()
		"""
		   TIME GEO                           Value
		0  2000 European Union (28 countries) NaN
		1  2001 European Union (28 countries) NaN
		36 2000 Euro area (18 countries)      NaN
		37 2001 Euro area (18 countries)      NaN
		48 2000 Euro area (17 countries)      NaN
		"""

		edu.max(axis=0)
		"""
		TIME 2011
		GEO Spain
		Value 8.81		
		"""

		edu['Value'].max()
		# 8.81

		"""
		count() Number of non-null observations
		sum() Sum of values
		mean() Mean of values
		median() Arithmetic median of values
		min() Minimum
		max() Maximum
		prod() Product of values
		std() Unbiased standard deviation
		var() Unbiased variance
		"""

		s = edu['Value']/100
		s.head()
		"""
		0 NaN
		1 NaN
		2 0.0500
		3 0.0503
		4 0.0495
		"""

		s = edu['Value'].apply(numpy.sqrt)
		s.head()
		"""
		0 NaN
		1 NaN
		2 2.236068
		3 2.242766
		4 2.224860
		"""

		edu['ValueNorm'] = edu['Value']/edu['Value'].max()
		edu.tail()
		"""
		    TIME GEO     Value ValueNorm
		379 2007 Finland 5.90  0.669694
		380 2008 Finland 6.10  0.692395
		381 2009 Finland 6.81  0.772985
		382 2010 Finland 6.85  0.777526
		383 2011 Finland 6.76  0.767310
		"""
