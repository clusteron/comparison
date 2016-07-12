

import numpy as np
import astropy
from astropy.io import ascii
from astropy.io import fits
from astropy.coordinates import SkyCoord
from astropy import units as u
import pylab
from pylab import plot
from astropy.cosmology import WMAP9 as cosmo
%pylab
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

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

print 'Plot ra x dec - sky'
ra_w = w['RAJ2000']*u.deg
dec_w = w['DEJ2000']*u.deg
pylab.plot(ra_w, dec_w, 'ro', label = 'Wen'),pylab.legend()

ra_r = r['RA']*u.deg 
dec_r = r['DEC']*u.deg
pylab.plot(ra_r, dec_r, 'bs', label = 'Redmapper'), pylab.xlabel('RA'), pylab.ylabel('DEC'), pylab.legend(),  pylab.title('Plotx Wen x Redmapper'), savefig('Plot-Sky.png'), close()
 
print 'catalog with values RA, DEC and z'
c_w = SkyCoord(ra = w['RAJ2000']*u.deg, dec = w['DEJ2000']*u.deg, distance = cosmo.comoving_distance(w['zph'])) 
c_r = SkyCoord(ra = r['RA']*u.deg, dec = r['DEC']*u.deg, distance = cosmo.comoving_distance(r['Z_LAMBDA'])) 

print 'Plot ra, dec and z - 3d'

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [w['RAJ2000']]
y = [w['DEJ2000']]
z = [w['zph']]

ax.scatter(x,y,z, c='r', marker = 'o')

ax.set_xlabel('RA')
ax.set_ylabel('DEC')
ax.set_zlabel('z')

savefig('Plot-3d-Wen.png'), close()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a = [r['RA']]
b = [r['DEC']]
c = [r['Z_LAMBDA']]

ax.scatter(a,b,c, c='b', marker = 's')

ax.set_xlabel('RA')
ax.set_ylabel('DEC')
ax.set_zlabel('z')

savefig('Plot-3d-Red.png'), close()

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
