import gl
import sys
print(sys.version)
print(gl.version())
gl.resetdefaults()
#open background image
gl.loadimage('mni152')
## Smooth interpolation of overlay 
gl.overlayloadsmooth(1)
#open disconnectome overlay
gl.overlayload("G:/.shortcut-targets-by-id/1du-K1whFNz4F791pBOvFGNOe-EBoIxzN/Articolo LOAD/mappe e immagini finali/multitasking_disconnectome_map_z.nii")
# set min to threshold for visualization
gl.minmax(1, 3, 15)
gl.opacity(1,70)
gl.colorname(1, '4hot')
gl.colorbarposition(1)
gl.colorbarsize(0.03)
# set mosaic slices for disconnectome hot spots
gl.mosaic("S A L- H -0.1 V -0.05 A -12 -8 5 15 20 30 35; C -45 -35 -25 -10 -3 2 10");
