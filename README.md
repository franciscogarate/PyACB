<h1>pyacb</h1>


:Date: 2013-12-04<br />
:Version: 1.1<br />
:Author: - Francisco Garate<br />

![Picture](http://www.garpa.net/wp-content/uploads/2013/07/author_googleplus_seo.png)

<hr>
<h2>Introduction</h2>
A python library for life sport calculations. Simple, powerful and easy-to-use.

<h2>Table of contents</h2>

* [Introduction](#introduction)
* [Quick Start](#quick-start)
* [Examples](#examples)
* Potential uses
* Installation

#<a name="introductions"></a>Introduction


**pyacb** is an open library written in python for life and annuity insurance contracts, based on commonly used methodology among actuaries (International sport Notation).

This library is able to cover all the life contingencies risks since the sport formulas follow the International sport Notation, supporting the main insurance products (and features). Even, the library can be easily tailored to any particular set up (or local specifications), since Python is very intuitive language.

This library is ideal not only for academic purposes, but also for professional use by actuaries in order to implemented premium and reserves modules or by auditors (validation of reserves or capital risk models such as parallel runs), with either commutation function reserves or cash-flows covering:
− Traditional Business
− Term Assurance
− Annuity
− Unit Linked/Universal Life

It is distributed as a single file module (lifecontingencies.py) and has no dependencies other than the Python Standard Library.

Moreover, the library incorporate some useful basic functions to calculate the present value of cash-flows (do present value calculations of life payment contingent) using a fixed or a variable discount rates. Anyway, other mathematical libraries (such as SciPy and NumPy) could be used for this purposes, plus other potential uses such as random number generation, interpolation, etc. Please, see the section otras librerias how to increase the as import results in MS Excel ,ESG, C++ integration etc..[see link libraries]
See :ref:

Additionally, the package includes several life mortality tables (mortalitytables.py), mainly extracted from academic books [see link books].

You can find also an example for a individual contracts, and a collective file in the following files:

`` python tariff-example1.py ``



This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. The author does not take any legal responsibility for the accuracy, completeness, or usefulness of the information herein.

<h2>Why Python?</h2>

Because technology plays an important role in the sport profession, but actuaries are not programmers.

Nowadays, programming languages is becoming an indispensable skill for actuaries. Python is a very clear, readable syntax, powerful and fast language. Easy learning, especially when you are not used to coding.

"Python lets you write the code you need, quickly. And, thanks to a highly optimized byte compiler and support libraries, Python code runs more than fast enough for most applications."
http://www.python.org/about/

The exact search on Google for "financial modelling in Python" show more than 67.000 results.

Python is sin duda es más facil que Excel y VBA. Curva de aprendizaje muy agradecida.

Consulta los tutoriales para instalar Python y un mainframe (Aptana Studio 3) en diferentes sistemas operaciones
  
#<a name="quick-start"></a>Quick Start

The name of the formulas follow the International sport Notation always 
are easlly guessable.
except for special character (as 'ä' are replace 'aa')

There are two smart formulas: annuity and A.

(Yes, I know that A is not the best name for a formula, but it's 

NOTE: annuity is only implemented for post-pay ?.

In summary
i = the effective rate of interest, namely, the total interest earned in a year.
x =
n =
Mortality Tables



Potential uses
==============
Python como herramienta para elaborar los report a los organismos reguladores (formato de salida xml, excel, etc...)


Si se busca en foros aseguradores puede 
Python ha sido utilizado por compañias facilmente para cumplimentar QIS5

Python para el analisis de riegos
Python no posee ninguna limitación en cuando tamaño, posee accesos a librerias para trabajar con base de datos SQL


Usos potenciales

- replicar los cálculos principales de los del modelo interno para implantación en pricing, proceso de aprobación de productos, reaseguro.
- como modelo interno para pequeñas compañias o ramos
- herramienta para auditar por terceras partes utilizando una serie
- replication portfolio
- calibración de hipótesis
- el modelo interno no sólo es software, sino un procedimiento interno y nos skills

Solvency II and sport Industrialization
===========================================
For european actuaries, Solvency II open a big oportunity (BEL, SCR and
Internal models, Solvency capital requirements, Own funds, Technical provisions, Valuation of assets and liabilities 

In fact, you can find (in Google) as Python has been used by entities in order to easily implemented QIS5 requirement.

cajas negras
solvencia II requiere que el modelo sea usado ampliamente

Los nuevos requisitos se traducen en:
- agilidad
- transversalidad

Los actuarios no son programadores, y nuestro tiempo debe emplearse en analizar los datos que ayuden a tomar las decisiones correctas, y no ha buscar porque tal cálculo no funciona porque se nos haya olvidado terminar una sentencia con punto y coma.


Los modelos internos deber util

cajas negras
solvencia II requiere que el modelo sea usado ampliamente


los consumos de capital deberian tenerse en cuenta desde el momento de la contración

Python es un lenguaje de programación didactico / academico.
Existe un gran número de librerias

Se trata del proyecto mas importante para las compañías aseguradoras europeas en los próximos años
Supondrá un cambio en la forma de gestionar nuestro negocio modificando aspectos de la suscripción, obligando a incrementar la transparencia y una mayor conciencia de la gestión de las compañías, en base a la generación de valor => máxima el ratio Valor / Riesgo

Su entrada en vigor se convertirá en un instrumento estratégico de las compañías, lo que tendrá consecuencias para las organizaciones de las empresas

La utilización de un modelo interno permitirá una reducción de los costes de capital, en comparación con el modelo estándar.

