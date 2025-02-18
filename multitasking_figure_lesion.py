
import gl
import sys
print(sys.version)
print(gl.version())
gl.resetdefaults()
#open background image
gl.loadimage('mni152')
## Smooth interpolation of overlay 
gl.overlayloadsmooth(1)
#open lesion overlay 
gl.overlayload("G:/.shortcut-targets-by-id/1du-K1whFNz4F791pBOvFGNOe-EBoIxzN/Articolo LOAD/mappe e immagini finali/multitasking_lesion_map_z.nii.gz")
# set min to threshold for visualization 
gl.minmax(1, 3, 13)
gl.opacity(1,70)
gl.colorname(1, '4hot')
gl.colorbarposition(1)
gl.colorbarsize(0.03)
# Set mosaic slices for lesions
gl.mosaic("S A L- H -0.1 V -0.05  A 0 10 20 30 40 50 60; C -30 -20 -15 -5 0 5 15");
# add X R 0 to add 3D render with slice reference) 
