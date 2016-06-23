import numpy as np
import matplotlib.pyplot as plt
import astropy
from astropy.io import ascii
from astropy.io import fits
from astropy.coordinates import SkyCoord
from astropy import units as u
import pylab
from pylab import plot
from astropy.cosmology import WMAP9 as cosmo
from astropy.cosmology import FlatLambdaCDM

print 'Reading files'
w = ascii.read('wen2012.csv') # leitura do catalogo wen
tr = fits.open('redmapper.fits') # leitura do catalogo redmapper
r = tr[1].data

#print w #imprimi o catalogo wen
#print r # imprimi o catalogo redmapper

c_w = SkyCoord(ra = w['col2']*u.degree, dec = w['col3']*u.degree) # Pega apenas os valores de ra e dec do catalogo wen
c_r = SkyCoord(ra = r['RA']*u.degree, dec = r['DEC']*u.degree) # Pega apenas os valores de ra e dec do catalogo redmapper

print 'match to catalog sky'
idx, d2d, d3d = c_w.match_to_catalog_sky(c_r) # mostra os matches do catalogo wen em relacao ao redmapper
#print idx, d2d, d3d #imprimi os valores
plot(d2d,d3d) # grafico do wen em relacao ao redmapper
pylab.xlabel('angle') #legenda pro eixo x
pylab.ylabel('quantity') #legenda pro eixo y
pylab.show() # mostra o grafico
# savefig

print 'match to catalog sky'
idx, d2d, d3d = c_r.match_to_catalog_sky(c_w) # mostra os matches do catalogo redmapper em relacao ao wen
#print idx, d2d, d3d #imprimi os valores
plot(d2d,d3d) # grafico do redmapper em relacao ao wen
pylab.xlabel('angle') #legenda pro eixo x
pylab.ylabel('quantity') #legenda pro eixo y
pylab.show() # mostra o grafico


c_w = SkyCoord(ra = w['col2']*u.deg, dec = w['col3']*u.deg, distance = cosmo.comoving_distance(w['col4']))  # Pega os valores de ra e dec e z, transformando o z em distancia
c_r = SkyCoord(ra = r['RA']*u.deg, dec = r['DEC']*u.deg, distance = cosmo.comoving_distance(r['Z_LAMBDA'])) # Pega os valores de ra e dec e z, transformando o z em distancia

idx, d2d, d3d = c_w.match_to_catalog_3d(c_r) #mostra os matches do catalogo de wen em relacao ao redmapper
#print idx, d2d, d3d #imprimi os valores
plot(d2d,d3d) # grafico do wen em relacao ao redmapper
pylab.xlabel('angle') #legenda pro eixo x
pylab.ylabel('quantity') #legenda pro eixo y
pylab.show() # mostra o grafico

idx, d2d, d3d = c_r.match_to_catalog_3d(c_w) #mostra os matches  do catalogo de redmapper em relacao ao wen
#print idx, d2d, d3d # imprimi os valores
plot(d2d,d3d) #grafico do redmapper em relacao ao wen
pylabel.xlabel('angle') #legenda pro eixo x
pylabel.ylabel('quantity') #legenda pro eixo y
pylab.show() # mostra o grafico


idxc_w, idxc_r, d2d, d3d = c_r.search_around_sky(c_w, 4*u.arcmin) # mostra os objetos em volta do catalogo de wen em relacao ao redmapper
#print idxc_w, idxc_r, d2d, d3d # imprimi os valores

idxc_w, idxc_r, d2d, d3d = c_w.search_around_sky(c_r, 4*u.arcmin) # mostra os objetos em volta do catalogo do redmapper em relacao ao wen
#print idxc_w, idxc_r, d2d, d3d # imprimi os valores

idxc_w, idxc_r, d2d, d3d = c_r.search_around_3d(c_w, 1000*u.kpc) # mostra os objetos em volta do catalogo de wen em relacao ao redmapper
#print idxc_w, idexc_r, d2d, d3d #imprimi os valores

idxc_w, idxc_r, d2d, d3d = c_w.search_around_3d(c_r, 1000*u.kpc) # mostra os objetos em volta do catalogo do redmapper em relacao ao wen
#print idxc_w, idexc_r, d2d, d3d #imprimi os valores 


