# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
maillagevtk = LegacyVTKReader(registrationName='maillage.vtk', FileNames=['../fichiers_resultats/maillage.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
maillagevtkDisplay = Show(maillagevtk, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
maillagevtkDisplay.Selection = None
maillagevtkDisplay.Representation = 'Outline'
maillagevtkDisplay.ColorArrayName = ['POINTS', '']
maillagevtkDisplay.LookupTable = None
maillagevtkDisplay.MapScalars = 1
maillagevtkDisplay.MultiComponentsMapping = 0
maillagevtkDisplay.InterpolateScalarsBeforeMapping = 1
maillagevtkDisplay.Opacity = 1.0
maillagevtkDisplay.PointSize = 2.0
maillagevtkDisplay.LineWidth = 1.0
maillagevtkDisplay.RenderLinesAsTubes = 0
maillagevtkDisplay.RenderPointsAsSpheres = 0
maillagevtkDisplay.Interpolation = 'Gouraud'
maillagevtkDisplay.Specular = 0.0
maillagevtkDisplay.SpecularColor = [1.0, 1.0, 1.0]
maillagevtkDisplay.SpecularPower = 100.0
maillagevtkDisplay.Luminosity = 0.0
maillagevtkDisplay.Ambient = 0.0
maillagevtkDisplay.Diffuse = 1.0
maillagevtkDisplay.Roughness = 0.3
maillagevtkDisplay.Metallic = 0.0
maillagevtkDisplay.EdgeTint = [1.0, 1.0, 1.0]
maillagevtkDisplay.Anisotropy = 0.0
maillagevtkDisplay.AnisotropyRotation = 0.0
maillagevtkDisplay.BaseIOR = 1.5
maillagevtkDisplay.CoatStrength = 0.0
maillagevtkDisplay.CoatIOR = 2.0
maillagevtkDisplay.CoatRoughness = 0.0
maillagevtkDisplay.CoatColor = [1.0, 1.0, 1.0]
maillagevtkDisplay.SelectTCoordArray = 'None'
maillagevtkDisplay.SelectNormalArray = 'None'
maillagevtkDisplay.SelectTangentArray = 'None'
maillagevtkDisplay.Texture = None
maillagevtkDisplay.RepeatTextures = 1
maillagevtkDisplay.InterpolateTextures = 0
maillagevtkDisplay.SeamlessU = 0
maillagevtkDisplay.SeamlessV = 0
maillagevtkDisplay.UseMipmapTextures = 0
maillagevtkDisplay.ShowTexturesOnBackface = 1
maillagevtkDisplay.BaseColorTexture = None
maillagevtkDisplay.NormalTexture = None
maillagevtkDisplay.NormalScale = 1.0
maillagevtkDisplay.CoatNormalTexture = None
maillagevtkDisplay.CoatNormalScale = 1.0
maillagevtkDisplay.MaterialTexture = None
maillagevtkDisplay.OcclusionStrength = 1.0
maillagevtkDisplay.AnisotropyTexture = None
maillagevtkDisplay.EmissiveTexture = None
maillagevtkDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
maillagevtkDisplay.FlipTextures = 0
maillagevtkDisplay.BackfaceRepresentation = 'Follow Frontface'
maillagevtkDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
maillagevtkDisplay.BackfaceOpacity = 1.0
maillagevtkDisplay.Position = [0.0, 0.0, 0.0]
maillagevtkDisplay.Scale = [1.0, 1.0, 1.0]
maillagevtkDisplay.Orientation = [0.0, 0.0, 0.0]
maillagevtkDisplay.Origin = [0.0, 0.0, 0.0]
maillagevtkDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
maillagevtkDisplay.Pickable = 1
maillagevtkDisplay.Triangulate = 0
maillagevtkDisplay.UseShaderReplacements = 0
maillagevtkDisplay.ShaderReplacements = ''
maillagevtkDisplay.NonlinearSubdivisionLevel = 1
maillagevtkDisplay.UseDataPartitions = 0
maillagevtkDisplay.OSPRayUseScaleArray = 'All Approximate'
maillagevtkDisplay.OSPRayScaleArray = ''
maillagevtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
maillagevtkDisplay.OSPRayMaterial = 'None'
maillagevtkDisplay.BlockSelectors = ['/']
maillagevtkDisplay.BlockColors = []
maillagevtkDisplay.BlockOpacities = []
maillagevtkDisplay.Orient = 0
maillagevtkDisplay.OrientationMode = 'Direction'
maillagevtkDisplay.SelectOrientationVectors = 'None'
maillagevtkDisplay.Scaling = 0
maillagevtkDisplay.ScaleMode = 'No Data Scaling Off'
maillagevtkDisplay.ScaleFactor = 5.0
maillagevtkDisplay.SelectScaleArray = 'None'
maillagevtkDisplay.GlyphType = 'Arrow'
maillagevtkDisplay.UseGlyphTable = 0
maillagevtkDisplay.GlyphTableIndexArray = 'None'
maillagevtkDisplay.UseCompositeGlyphTable = 0
maillagevtkDisplay.UseGlyphCullingAndLOD = 0
maillagevtkDisplay.LODValues = []
maillagevtkDisplay.ColorByLODIndex = 0
maillagevtkDisplay.GaussianRadius = 0.25
maillagevtkDisplay.ShaderPreset = 'Sphere'
maillagevtkDisplay.CustomTriangleScale = 3
maillagevtkDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
maillagevtkDisplay.Emissive = 0
maillagevtkDisplay.ScaleByArray = 0
maillagevtkDisplay.SetScaleArray = [None, '']
maillagevtkDisplay.ScaleArrayComponent = 0
maillagevtkDisplay.UseScaleFunction = 1
maillagevtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
maillagevtkDisplay.OpacityByArray = 0
maillagevtkDisplay.OpacityArray = [None, '']
maillagevtkDisplay.OpacityArrayComponent = 0
maillagevtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
maillagevtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
maillagevtkDisplay.SelectionCellLabelBold = 0
maillagevtkDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
maillagevtkDisplay.SelectionCellLabelFontFamily = 'Arial'
maillagevtkDisplay.SelectionCellLabelFontFile = ''
maillagevtkDisplay.SelectionCellLabelFontSize = 18
maillagevtkDisplay.SelectionCellLabelItalic = 0
maillagevtkDisplay.SelectionCellLabelJustification = 'Left'
maillagevtkDisplay.SelectionCellLabelOpacity = 1.0
maillagevtkDisplay.SelectionCellLabelShadow = 0
maillagevtkDisplay.SelectionPointLabelBold = 0
maillagevtkDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
maillagevtkDisplay.SelectionPointLabelFontFamily = 'Arial'
maillagevtkDisplay.SelectionPointLabelFontFile = ''
maillagevtkDisplay.SelectionPointLabelFontSize = 18
maillagevtkDisplay.SelectionPointLabelItalic = 0
maillagevtkDisplay.SelectionPointLabelJustification = 'Left'
maillagevtkDisplay.SelectionPointLabelOpacity = 1.0
maillagevtkDisplay.SelectionPointLabelShadow = 0
maillagevtkDisplay.PolarAxes = 'PolarAxesRepresentation'
maillagevtkDisplay.ScalarOpacityFunction = None
maillagevtkDisplay.ScalarOpacityUnitDistance = 2.398852817515995
maillagevtkDisplay.SelectMapper = 'Projected tetra'
maillagevtkDisplay.SamplingDimensions = [128, 128, 128]

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
maillagevtkDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
maillagevtkDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
maillagevtkDisplay.GlyphType.TipResolution = 6
maillagevtkDisplay.GlyphType.TipRadius = 0.1
maillagevtkDisplay.GlyphType.TipLength = 0.35
maillagevtkDisplay.GlyphType.ShaftResolution = 6
maillagevtkDisplay.GlyphType.ShaftRadius = 0.03
maillagevtkDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
maillagevtkDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
maillagevtkDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
maillagevtkDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
maillagevtkDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
maillagevtkDisplay.DataAxesGrid.XTitle = 'X Axis'
maillagevtkDisplay.DataAxesGrid.YTitle = 'Y Axis'
maillagevtkDisplay.DataAxesGrid.ZTitle = 'Z Axis'
maillagevtkDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
maillagevtkDisplay.DataAxesGrid.XTitleFontFile = ''
maillagevtkDisplay.DataAxesGrid.XTitleBold = 0
maillagevtkDisplay.DataAxesGrid.XTitleItalic = 0
maillagevtkDisplay.DataAxesGrid.XTitleFontSize = 12
maillagevtkDisplay.DataAxesGrid.XTitleShadow = 0
maillagevtkDisplay.DataAxesGrid.XTitleOpacity = 1.0
maillagevtkDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
maillagevtkDisplay.DataAxesGrid.YTitleFontFile = ''
maillagevtkDisplay.DataAxesGrid.YTitleBold = 0
maillagevtkDisplay.DataAxesGrid.YTitleItalic = 0
maillagevtkDisplay.DataAxesGrid.YTitleFontSize = 12
maillagevtkDisplay.DataAxesGrid.YTitleShadow = 0
maillagevtkDisplay.DataAxesGrid.YTitleOpacity = 1.0
maillagevtkDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
maillagevtkDisplay.DataAxesGrid.ZTitleFontFile = ''
maillagevtkDisplay.DataAxesGrid.ZTitleBold = 0
maillagevtkDisplay.DataAxesGrid.ZTitleItalic = 0
maillagevtkDisplay.DataAxesGrid.ZTitleFontSize = 12
maillagevtkDisplay.DataAxesGrid.ZTitleShadow = 0
maillagevtkDisplay.DataAxesGrid.ZTitleOpacity = 1.0
maillagevtkDisplay.DataAxesGrid.FacesToRender = 63
maillagevtkDisplay.DataAxesGrid.CullBackface = 0
maillagevtkDisplay.DataAxesGrid.CullFrontface = 1
maillagevtkDisplay.DataAxesGrid.ShowGrid = 0
maillagevtkDisplay.DataAxesGrid.ShowEdges = 1
maillagevtkDisplay.DataAxesGrid.ShowTicks = 1
maillagevtkDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
maillagevtkDisplay.DataAxesGrid.AxesToLabel = 63
maillagevtkDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
maillagevtkDisplay.DataAxesGrid.XLabelFontFile = ''
maillagevtkDisplay.DataAxesGrid.XLabelBold = 0
maillagevtkDisplay.DataAxesGrid.XLabelItalic = 0
maillagevtkDisplay.DataAxesGrid.XLabelFontSize = 12
maillagevtkDisplay.DataAxesGrid.XLabelShadow = 0
maillagevtkDisplay.DataAxesGrid.XLabelOpacity = 1.0
maillagevtkDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
maillagevtkDisplay.DataAxesGrid.YLabelFontFile = ''
maillagevtkDisplay.DataAxesGrid.YLabelBold = 0
maillagevtkDisplay.DataAxesGrid.YLabelItalic = 0
maillagevtkDisplay.DataAxesGrid.YLabelFontSize = 12
maillagevtkDisplay.DataAxesGrid.YLabelShadow = 0
maillagevtkDisplay.DataAxesGrid.YLabelOpacity = 1.0
maillagevtkDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
maillagevtkDisplay.DataAxesGrid.ZLabelFontFile = ''
maillagevtkDisplay.DataAxesGrid.ZLabelBold = 0
maillagevtkDisplay.DataAxesGrid.ZLabelItalic = 0
maillagevtkDisplay.DataAxesGrid.ZLabelFontSize = 12
maillagevtkDisplay.DataAxesGrid.ZLabelShadow = 0
maillagevtkDisplay.DataAxesGrid.ZLabelOpacity = 1.0
maillagevtkDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
maillagevtkDisplay.DataAxesGrid.XAxisPrecision = 2
maillagevtkDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
maillagevtkDisplay.DataAxesGrid.XAxisLabels = []
maillagevtkDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
maillagevtkDisplay.DataAxesGrid.YAxisPrecision = 2
maillagevtkDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
maillagevtkDisplay.DataAxesGrid.YAxisLabels = []
maillagevtkDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
maillagevtkDisplay.DataAxesGrid.ZAxisPrecision = 2
maillagevtkDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
maillagevtkDisplay.DataAxesGrid.ZAxisLabels = []
maillagevtkDisplay.DataAxesGrid.UseCustomBounds = 0
maillagevtkDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
maillagevtkDisplay.PolarAxes.Visibility = 0
maillagevtkDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
maillagevtkDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
maillagevtkDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
maillagevtkDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
maillagevtkDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
maillagevtkDisplay.PolarAxes.EnableCustomRange = 0
maillagevtkDisplay.PolarAxes.CustomRange = [0.0, 1.0]
maillagevtkDisplay.PolarAxes.PolarAxisVisibility = 1
maillagevtkDisplay.PolarAxes.RadialAxesVisibility = 1
maillagevtkDisplay.PolarAxes.DrawRadialGridlines = 1
maillagevtkDisplay.PolarAxes.PolarArcsVisibility = 1
maillagevtkDisplay.PolarAxes.DrawPolarArcsGridlines = 1
maillagevtkDisplay.PolarAxes.NumberOfRadialAxes = 0
maillagevtkDisplay.PolarAxes.AutoSubdividePolarAxis = 1
maillagevtkDisplay.PolarAxes.NumberOfPolarAxis = 0
maillagevtkDisplay.PolarAxes.MinimumRadius = 0.0
maillagevtkDisplay.PolarAxes.MinimumAngle = 0.0
maillagevtkDisplay.PolarAxes.MaximumAngle = 90.0
maillagevtkDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
maillagevtkDisplay.PolarAxes.Ratio = 1.0
maillagevtkDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
maillagevtkDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
maillagevtkDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
maillagevtkDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
maillagevtkDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
maillagevtkDisplay.PolarAxes.PolarAxisTitleVisibility = 1
maillagevtkDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
maillagevtkDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
maillagevtkDisplay.PolarAxes.PolarLabelVisibility = 1
maillagevtkDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
maillagevtkDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
maillagevtkDisplay.PolarAxes.RadialLabelVisibility = 1
maillagevtkDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
maillagevtkDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
maillagevtkDisplay.PolarAxes.RadialUnitsVisibility = 1
maillagevtkDisplay.PolarAxes.ScreenSize = 10.0
maillagevtkDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
maillagevtkDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
maillagevtkDisplay.PolarAxes.PolarAxisTitleFontFile = ''
maillagevtkDisplay.PolarAxes.PolarAxisTitleBold = 0
maillagevtkDisplay.PolarAxes.PolarAxisTitleItalic = 0
maillagevtkDisplay.PolarAxes.PolarAxisTitleShadow = 0
maillagevtkDisplay.PolarAxes.PolarAxisTitleFontSize = 12
maillagevtkDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
maillagevtkDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
maillagevtkDisplay.PolarAxes.PolarAxisLabelFontFile = ''
maillagevtkDisplay.PolarAxes.PolarAxisLabelBold = 0
maillagevtkDisplay.PolarAxes.PolarAxisLabelItalic = 0
maillagevtkDisplay.PolarAxes.PolarAxisLabelShadow = 0
maillagevtkDisplay.PolarAxes.PolarAxisLabelFontSize = 12
maillagevtkDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
maillagevtkDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
maillagevtkDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
maillagevtkDisplay.PolarAxes.LastRadialAxisTextBold = 0
maillagevtkDisplay.PolarAxes.LastRadialAxisTextItalic = 0
maillagevtkDisplay.PolarAxes.LastRadialAxisTextShadow = 0
maillagevtkDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
maillagevtkDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
maillagevtkDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
maillagevtkDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
maillagevtkDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
maillagevtkDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
maillagevtkDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
maillagevtkDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
maillagevtkDisplay.PolarAxes.EnableDistanceLOD = 1
maillagevtkDisplay.PolarAxes.DistanceLODThreshold = 0.7
maillagevtkDisplay.PolarAxes.EnableViewAngleLOD = 1
maillagevtkDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
maillagevtkDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
maillagevtkDisplay.PolarAxes.PolarTicksVisibility = 1
maillagevtkDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
maillagevtkDisplay.PolarAxes.TickLocation = 'Both'
maillagevtkDisplay.PolarAxes.AxisTickVisibility = 1
maillagevtkDisplay.PolarAxes.AxisMinorTickVisibility = 0
maillagevtkDisplay.PolarAxes.ArcTickVisibility = 1
maillagevtkDisplay.PolarAxes.ArcMinorTickVisibility = 0
maillagevtkDisplay.PolarAxes.DeltaAngleMajor = 10.0
maillagevtkDisplay.PolarAxes.DeltaAngleMinor = 5.0
maillagevtkDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
maillagevtkDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
maillagevtkDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
maillagevtkDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
maillagevtkDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
maillagevtkDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
maillagevtkDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
maillagevtkDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
maillagevtkDisplay.PolarAxes.ArcMajorTickSize = 0.0
maillagevtkDisplay.PolarAxes.ArcTickRatioSize = 0.3
maillagevtkDisplay.PolarAxes.ArcMajorTickThickness = 1.0
maillagevtkDisplay.PolarAxes.ArcTickRatioThickness = 0.5
maillagevtkDisplay.PolarAxes.Use2DMode = 0
maillagevtkDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# change representation type
maillagevtkDisplay.SetRepresentationType('Surface With Edges')

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1048, 608)

# current camera placement for renderView1
renderView1.CameraPosition = [78.86300231498385, 60.89305713856357, 98.88635748327832]
renderView1.CameraFocalPoint = [25.0, 4.999999999999999, 14.999999999999995]
renderView1.CameraViewUp = [-0.18564789365386244, 0.868553893061659, -0.4595095150585249]
renderView1.CameraParallelScale = 29.58039891549808

# save screenshot
SaveScreenshot('../visualisation_graphiques/maillage3D.png', renderView1, ImageResolution=[1048, 608],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5',
    MetaData=['Application', 'ParaView'])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1048, 608)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [78.86300231498385, 60.89305713856357, 98.88635748327832]
renderView1.CameraFocalPoint = [25.0, 4.999999999999999, 14.999999999999995]
renderView1.CameraViewUp = [-0.18564789365386244, 0.868553893061659, -0.4595095150585249]
renderView1.CameraParallelScale = 29.58039891549808

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).