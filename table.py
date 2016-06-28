
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

print 'Reading files'
w = ascii.read('wen.csv') 
r = fits.open('redmapper.fits') 
r = r[1].data

#print w 
#print r 

print 'catalog with values RA and DEC'
cw = SkyCoord(ra = w['RAJ2000']*u.degree, dec = w['DEJ2000']*u.degree) 
cr = SkyCoord(ra = r['RA']*u.degree, dec = r['DEC']*u.degree) 

print 'match to catalog sky'
idx, d2d, d3d = cw.match_to_catalog_sky(cr) 
#print idx, d2d, d3d 


print 'match to catalog sky'
idx, d2d, d3d = cr.match_to_catalog_sky(cw) 
#print idx, d2d, d3d 

print 'catalog with values RA, DEC and z'
c_w = SkyCoord(ra = w['RAJ2000']*u.deg, dec = w['DEJ2000']*u.deg, distance = cosmo.comoving_distance(w['zph'])) 
c_r = SkyCoord(ra = r['RA']*u.deg, dec = r['DEC']*u.deg, distance = cosmo.comoving_distance(r['Z_LAMBDA'])) 

print 'match to catalog 3d'
idx, d2d, d3d = c_w.match_to_catalog_3d(c_r) 
#print idx, d2d, d3d 

print 'match to catalog 3d'
idx, d2d, d3d = c_r.match_to_catalog_3d(c_w) 
#print idx, d2d, d3d 

print 'Objects around to catalog sky'
idxcw, idxcr, d2d, d3d = cr.search_around_sky(cw, 4*u.arcmin)
#print idxc_w, idxc_r, d2d, d3d 

idxcw, idxcr, d2d, d3d = cw.search_around_sky(cr, 4*u.arcmin)
#print idxc_w, idxc_r, d2d, d3d 

print 'Objects around to catalog 3d'
idxc_w, idxc_r, d2d, d3d = c_r.search_around_3d(c_w, 1000*u.kpc) 
#print idxc_w, idexc_r, d2d, d3d

idxc_w, idxc_r, d2d, d3d = c_w.search_around_3d(c_r, 1000*u.kpc)
#print idxc_w, idexc_r, d2d, d3d  
