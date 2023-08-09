
import gl
import sys
print(sys.version)
print(gl.version())
gl.resetdefaults()
#open background image
gl.loadimage('spm152')
## Smooth interpolation of overlay 
gl.overlayloadsmooth(1)
#open lesion overlay 
#gl.overlayload('G:/.shortcut-targets-by-id/1du-K1whFNz4F791pBOvFGNOe-EBoIxzN/Articolo LOAD/mappe e immagini di prova/2023 Lesioni con covariate 01.nii')
gl.overlayload('G:/.shortcut-targets-by-id/1du-K1whFNz4F791pBOvFGNOe-EBoIxzN/Articolo LOAD/mappe e immagini di prova/lesion_map_z.nii')
# set min to threshold for visualization 
gl.minmax(1, 1.5, 4.73593)
gl.opacity(1,70)
gl.colorname(1, '4hot')
gl.colorbarposition(1)
gl.colorbarsize(0.03)
# Set mosaic slices for lesions
gl.mosaic("S A L- H -0.1 V -0.05  0 10 20 30 40 50 60; C -30 -20 -15 -5 0 5 15");
# add X R 0 to add 3D render with slice reference) 
