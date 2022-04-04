# trace generated using paraview version 5.10.0-RC1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Pour lire le fichier config
with open('../../simu.cfg', newline='') as cfgfile:
    reader = cfgfile.read()
    reader = reader.replace("\r\n", " ").split(" ")
    config = {}
    for key, val in zip(reader[0::2], reader[1::2]):
        config[key] = val
  
filename=[]
for n in range(int(config["N"])+1):
  filename+=['../fichiers_resultats/solution3D_instat_flux_constant/solution3D_flux_constant.'+str(n)+'.vtk']

# create a new 'Legacy VTK Reader'
solution3D_flux_constant = LegacyVTKReader(registrationName='solution3D_flux_constant.*', FileNames=filename)

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# set active source
SetActiveSource(solution3D_flux_constant)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
solution3D_flux_constantDisplay = Show(solution3D_flux_constant, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
solution3D_flux_constantDisplay.Selection = None
solution3D_flux_constantDisplay.Representation = 'Outline'
solution3D_flux_constantDisplay.ColorArrayName = [None, '']
solution3D_flux_constantDisplay.LookupTable = None
solution3D_flux_constantDisplay.MapScalars = 1
solution3D_flux_constantDisplay.MultiComponentsMapping = 0
solution3D_flux_constantDisplay.InterpolateScalarsBeforeMapping = 1
solution3D_flux_constantDisplay.Opacity = 1.0
solution3D_flux_constantDisplay.PointSize = 2.0
solution3D_flux_constantDisplay.LineWidth = 1.0
solution3D_flux_constantDisplay.RenderLinesAsTubes = 0
solution3D_flux_constantDisplay.RenderPointsAsSpheres = 0
solution3D_flux_constantDisplay.Interpolation = 'Gouraud'
solution3D_flux_constantDisplay.Specular = 0.0
solution3D_flux_constantDisplay.SpecularColor = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.SpecularPower = 100.0
solution3D_flux_constantDisplay.Luminosity = 0.0
solution3D_flux_constantDisplay.Ambient = 0.0
solution3D_flux_constantDisplay.Diffuse = 1.0
solution3D_flux_constantDisplay.Roughness = 0.3
solution3D_flux_constantDisplay.Metallic = 0.0
solution3D_flux_constantDisplay.EdgeTint = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.Anisotropy = 0.0
solution3D_flux_constantDisplay.AnisotropyRotation = 0.0
solution3D_flux_constantDisplay.BaseIOR = 1.5
solution3D_flux_constantDisplay.CoatStrength = 0.0
solution3D_flux_constantDisplay.CoatIOR = 2.0
solution3D_flux_constantDisplay.CoatRoughness = 0.0
solution3D_flux_constantDisplay.CoatColor = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.SelectTCoordArray = 'None'
solution3D_flux_constantDisplay.SelectNormalArray = 'None'
solution3D_flux_constantDisplay.SelectTangentArray = 'None'
solution3D_flux_constantDisplay.Texture = None
solution3D_flux_constantDisplay.RepeatTextures = 1
solution3D_flux_constantDisplay.InterpolateTextures = 0
solution3D_flux_constantDisplay.SeamlessU = 0
solution3D_flux_constantDisplay.SeamlessV = 0
solution3D_flux_constantDisplay.UseMipmapTextures = 0
solution3D_flux_constantDisplay.ShowTexturesOnBackface = 1
solution3D_flux_constantDisplay.BaseColorTexture = None
solution3D_flux_constantDisplay.NormalTexture = None
solution3D_flux_constantDisplay.NormalScale = 1.0
solution3D_flux_constantDisplay.CoatNormalTexture = None
solution3D_flux_constantDisplay.CoatNormalScale = 1.0
solution3D_flux_constantDisplay.MaterialTexture = None
solution3D_flux_constantDisplay.OcclusionStrength = 1.0
solution3D_flux_constantDisplay.AnisotropyTexture = None
solution3D_flux_constantDisplay.EmissiveTexture = None
solution3D_flux_constantDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.FlipTextures = 0
solution3D_flux_constantDisplay.BackfaceRepresentation = 'Follow Frontface'
solution3D_flux_constantDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.BackfaceOpacity = 1.0
solution3D_flux_constantDisplay.Position = [0.0, 0.0, 0.0]
solution3D_flux_constantDisplay.Scale = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.Orientation = [0.0, 0.0, 0.0]
solution3D_flux_constantDisplay.Origin = [0.0, 0.0, 0.0]
solution3D_flux_constantDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
solution3D_flux_constantDisplay.Pickable = 1
solution3D_flux_constantDisplay.Triangulate = 0
solution3D_flux_constantDisplay.UseShaderReplacements = 0
solution3D_flux_constantDisplay.ShaderReplacements = ''
solution3D_flux_constantDisplay.NonlinearSubdivisionLevel = 1
solution3D_flux_constantDisplay.UseDataPartitions = 0
solution3D_flux_constantDisplay.OSPRayUseScaleArray = 'All Approximate'
solution3D_flux_constantDisplay.OSPRayScaleArray = 'sol1'
solution3D_flux_constantDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
solution3D_flux_constantDisplay.OSPRayMaterial = 'None'
solution3D_flux_constantDisplay.BlockSelectors = ['/']
solution3D_flux_constantDisplay.BlockColors = []
solution3D_flux_constantDisplay.BlockOpacities = []
solution3D_flux_constantDisplay.Orient = 0
solution3D_flux_constantDisplay.OrientationMode = 'Direction'
solution3D_flux_constantDisplay.SelectOrientationVectors = 'None'
solution3D_flux_constantDisplay.Scaling = 0
solution3D_flux_constantDisplay.ScaleMode = 'No Data Scaling Off'
solution3D_flux_constantDisplay.ScaleFactor = 5.0
solution3D_flux_constantDisplay.SelectScaleArray = 'None'
solution3D_flux_constantDisplay.GlyphType = 'Arrow'
solution3D_flux_constantDisplay.UseGlyphTable = 0
solution3D_flux_constantDisplay.GlyphTableIndexArray = 'None'
solution3D_flux_constantDisplay.UseCompositeGlyphTable = 0
solution3D_flux_constantDisplay.UseGlyphCullingAndLOD = 0
solution3D_flux_constantDisplay.LODValues = []
solution3D_flux_constantDisplay.ColorByLODIndex = 0
solution3D_flux_constantDisplay.GaussianRadius = 0.25
solution3D_flux_constantDisplay.ShaderPreset = 'Sphere'
solution3D_flux_constantDisplay.CustomTriangleScale = 3
solution3D_flux_constantDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
solution3D_flux_constantDisplay.Emissive = 0
solution3D_flux_constantDisplay.ScaleByArray = 0
solution3D_flux_constantDisplay.SetScaleArray = ['POINTS', 'sol1']
solution3D_flux_constantDisplay.ScaleArrayComponent = ''
solution3D_flux_constantDisplay.UseScaleFunction = 1
solution3D_flux_constantDisplay.ScaleTransferFunction = 'PiecewiseFunction'
solution3D_flux_constantDisplay.OpacityByArray = 0
solution3D_flux_constantDisplay.OpacityArray = ['POINTS', 'sol1']
solution3D_flux_constantDisplay.OpacityArrayComponent = ''
solution3D_flux_constantDisplay.OpacityTransferFunction = 'PiecewiseFunction'
solution3D_flux_constantDisplay.DataAxesGrid = 'GridAxesRepresentation'
solution3D_flux_constantDisplay.SelectionCellLabelBold = 0
solution3D_flux_constantDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
solution3D_flux_constantDisplay.SelectionCellLabelFontFamily = 'Arial'
solution3D_flux_constantDisplay.SelectionCellLabelFontFile = ''
solution3D_flux_constantDisplay.SelectionCellLabelFontSize = 18
solution3D_flux_constantDisplay.SelectionCellLabelItalic = 0
solution3D_flux_constantDisplay.SelectionCellLabelJustification = 'Left'
solution3D_flux_constantDisplay.SelectionCellLabelOpacity = 1.0
solution3D_flux_constantDisplay.SelectionCellLabelShadow = 0
solution3D_flux_constantDisplay.SelectionPointLabelBold = 0
solution3D_flux_constantDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
solution3D_flux_constantDisplay.SelectionPointLabelFontFamily = 'Arial'
solution3D_flux_constantDisplay.SelectionPointLabelFontFile = ''
solution3D_flux_constantDisplay.SelectionPointLabelFontSize = 18
solution3D_flux_constantDisplay.SelectionPointLabelItalic = 0
solution3D_flux_constantDisplay.SelectionPointLabelJustification = 'Left'
solution3D_flux_constantDisplay.SelectionPointLabelOpacity = 1.0
solution3D_flux_constantDisplay.SelectionPointLabelShadow = 0
solution3D_flux_constantDisplay.PolarAxes = 'PolarAxesRepresentation'
solution3D_flux_constantDisplay.ScalarOpacityFunction = None
solution3D_flux_constantDisplay.ScalarOpacityUnitDistance = 2.398852817515995
solution3D_flux_constantDisplay.SelectMapper = 'Projected tetra'
solution3D_flux_constantDisplay.SamplingDimensions = [128, 128, 128]

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
solution3D_flux_constantDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
solution3D_flux_constantDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
solution3D_flux_constantDisplay.GlyphType.TipResolution = 6
solution3D_flux_constantDisplay.GlyphType.TipRadius = 0.1
solution3D_flux_constantDisplay.GlyphType.TipLength = 0.35
solution3D_flux_constantDisplay.GlyphType.ShaftResolution = 6
solution3D_flux_constantDisplay.GlyphType.ShaftRadius = 0.03
solution3D_flux_constantDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
solution3D_flux_constantDisplay.ScaleTransferFunction.Points = [20.0, 0.0, 0.5, 0.0, 20.00390625, 1.0, 0.5, 0.0]
solution3D_flux_constantDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
solution3D_flux_constantDisplay.OpacityTransferFunction.Points = [20.0, 0.0, 0.5, 0.0, 20.00390625, 1.0, 0.5, 0.0]
solution3D_flux_constantDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
solution3D_flux_constantDisplay.DataAxesGrid.XTitle = 'X Axis'
solution3D_flux_constantDisplay.DataAxesGrid.YTitle = 'Y Axis'
solution3D_flux_constantDisplay.DataAxesGrid.ZTitle = 'Z Axis'
solution3D_flux_constantDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
solution3D_flux_constantDisplay.DataAxesGrid.XTitleFontFile = ''
solution3D_flux_constantDisplay.DataAxesGrid.XTitleBold = 0
solution3D_flux_constantDisplay.DataAxesGrid.XTitleItalic = 0
solution3D_flux_constantDisplay.DataAxesGrid.XTitleFontSize = 12
solution3D_flux_constantDisplay.DataAxesGrid.XTitleShadow = 0
solution3D_flux_constantDisplay.DataAxesGrid.XTitleOpacity = 1.0
solution3D_flux_constantDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
solution3D_flux_constantDisplay.DataAxesGrid.YTitleFontFile = ''
solution3D_flux_constantDisplay.DataAxesGrid.YTitleBold = 0
solution3D_flux_constantDisplay.DataAxesGrid.YTitleItalic = 0
solution3D_flux_constantDisplay.DataAxesGrid.YTitleFontSize = 12
solution3D_flux_constantDisplay.DataAxesGrid.YTitleShadow = 0
solution3D_flux_constantDisplay.DataAxesGrid.YTitleOpacity = 1.0
solution3D_flux_constantDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
solution3D_flux_constantDisplay.DataAxesGrid.ZTitleFontFile = ''
solution3D_flux_constantDisplay.DataAxesGrid.ZTitleBold = 0
solution3D_flux_constantDisplay.DataAxesGrid.ZTitleItalic = 0
solution3D_flux_constantDisplay.DataAxesGrid.ZTitleFontSize = 12
solution3D_flux_constantDisplay.DataAxesGrid.ZTitleShadow = 0
solution3D_flux_constantDisplay.DataAxesGrid.ZTitleOpacity = 1.0
solution3D_flux_constantDisplay.DataAxesGrid.FacesToRender = 63
solution3D_flux_constantDisplay.DataAxesGrid.CullBackface = 0
solution3D_flux_constantDisplay.DataAxesGrid.CullFrontface = 1
solution3D_flux_constantDisplay.DataAxesGrid.ShowGrid = 0
solution3D_flux_constantDisplay.DataAxesGrid.ShowEdges = 1
solution3D_flux_constantDisplay.DataAxesGrid.ShowTicks = 1
solution3D_flux_constantDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
solution3D_flux_constantDisplay.DataAxesGrid.AxesToLabel = 63
solution3D_flux_constantDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
solution3D_flux_constantDisplay.DataAxesGrid.XLabelFontFile = ''
solution3D_flux_constantDisplay.DataAxesGrid.XLabelBold = 0
solution3D_flux_constantDisplay.DataAxesGrid.XLabelItalic = 0
solution3D_flux_constantDisplay.DataAxesGrid.XLabelFontSize = 12
solution3D_flux_constantDisplay.DataAxesGrid.XLabelShadow = 0
solution3D_flux_constantDisplay.DataAxesGrid.XLabelOpacity = 1.0
solution3D_flux_constantDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
solution3D_flux_constantDisplay.DataAxesGrid.YLabelFontFile = ''
solution3D_flux_constantDisplay.DataAxesGrid.YLabelBold = 0
solution3D_flux_constantDisplay.DataAxesGrid.YLabelItalic = 0
solution3D_flux_constantDisplay.DataAxesGrid.YLabelFontSize = 12
solution3D_flux_constantDisplay.DataAxesGrid.YLabelShadow = 0
solution3D_flux_constantDisplay.DataAxesGrid.YLabelOpacity = 1.0
solution3D_flux_constantDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
solution3D_flux_constantDisplay.DataAxesGrid.ZLabelFontFile = ''
solution3D_flux_constantDisplay.DataAxesGrid.ZLabelBold = 0
solution3D_flux_constantDisplay.DataAxesGrid.ZLabelItalic = 0
solution3D_flux_constantDisplay.DataAxesGrid.ZLabelFontSize = 12
solution3D_flux_constantDisplay.DataAxesGrid.ZLabelShadow = 0
solution3D_flux_constantDisplay.DataAxesGrid.ZLabelOpacity = 1.0
solution3D_flux_constantDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
solution3D_flux_constantDisplay.DataAxesGrid.XAxisPrecision = 2
solution3D_flux_constantDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
solution3D_flux_constantDisplay.DataAxesGrid.XAxisLabels = []
solution3D_flux_constantDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
solution3D_flux_constantDisplay.DataAxesGrid.YAxisPrecision = 2
solution3D_flux_constantDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
solution3D_flux_constantDisplay.DataAxesGrid.YAxisLabels = []
solution3D_flux_constantDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
solution3D_flux_constantDisplay.DataAxesGrid.ZAxisPrecision = 2
solution3D_flux_constantDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
solution3D_flux_constantDisplay.DataAxesGrid.ZAxisLabels = []
solution3D_flux_constantDisplay.DataAxesGrid.UseCustomBounds = 0
solution3D_flux_constantDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
solution3D_flux_constantDisplay.PolarAxes.Visibility = 0
solution3D_flux_constantDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
solution3D_flux_constantDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
solution3D_flux_constantDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
solution3D_flux_constantDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
solution3D_flux_constantDisplay.PolarAxes.EnableCustomRange = 0
solution3D_flux_constantDisplay.PolarAxes.CustomRange = [0.0, 1.0]
solution3D_flux_constantDisplay.PolarAxes.PolarAxisVisibility = 1
solution3D_flux_constantDisplay.PolarAxes.RadialAxesVisibility = 1
solution3D_flux_constantDisplay.PolarAxes.DrawRadialGridlines = 1
solution3D_flux_constantDisplay.PolarAxes.PolarArcsVisibility = 1
solution3D_flux_constantDisplay.PolarAxes.DrawPolarArcsGridlines = 1
solution3D_flux_constantDisplay.PolarAxes.NumberOfRadialAxes = 0
solution3D_flux_constantDisplay.PolarAxes.AutoSubdividePolarAxis = 1
solution3D_flux_constantDisplay.PolarAxes.NumberOfPolarAxis = 0
solution3D_flux_constantDisplay.PolarAxes.MinimumRadius = 0.0
solution3D_flux_constantDisplay.PolarAxes.MinimumAngle = 0.0
solution3D_flux_constantDisplay.PolarAxes.MaximumAngle = 90.0
solution3D_flux_constantDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
solution3D_flux_constantDisplay.PolarAxes.Ratio = 1.0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTitleVisibility = 1
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
solution3D_flux_constantDisplay.PolarAxes.PolarLabelVisibility = 1
solution3D_flux_constantDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
solution3D_flux_constantDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
solution3D_flux_constantDisplay.PolarAxes.RadialLabelVisibility = 1
solution3D_flux_constantDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
solution3D_flux_constantDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
solution3D_flux_constantDisplay.PolarAxes.RadialUnitsVisibility = 1
solution3D_flux_constantDisplay.PolarAxes.ScreenSize = 10.0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTitleFontFile = ''
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTitleBold = 0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTitleItalic = 0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTitleShadow = 0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTitleFontSize = 12
solution3D_flux_constantDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
solution3D_flux_constantDisplay.PolarAxes.PolarAxisLabelFontFile = ''
solution3D_flux_constantDisplay.PolarAxes.PolarAxisLabelBold = 0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisLabelItalic = 0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisLabelShadow = 0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisLabelFontSize = 12
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisTextBold = 0
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisTextItalic = 0
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisTextShadow = 0
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
solution3D_flux_constantDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
solution3D_flux_constantDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
solution3D_flux_constantDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
solution3D_flux_constantDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
solution3D_flux_constantDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
solution3D_flux_constantDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
solution3D_flux_constantDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
solution3D_flux_constantDisplay.PolarAxes.EnableDistanceLOD = 1
solution3D_flux_constantDisplay.PolarAxes.DistanceLODThreshold = 0.7
solution3D_flux_constantDisplay.PolarAxes.EnableViewAngleLOD = 1
solution3D_flux_constantDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
solution3D_flux_constantDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
solution3D_flux_constantDisplay.PolarAxes.PolarTicksVisibility = 1
solution3D_flux_constantDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
solution3D_flux_constantDisplay.PolarAxes.TickLocation = 'Both'
solution3D_flux_constantDisplay.PolarAxes.AxisTickVisibility = 1
solution3D_flux_constantDisplay.PolarAxes.AxisMinorTickVisibility = 0
solution3D_flux_constantDisplay.PolarAxes.ArcTickVisibility = 1
solution3D_flux_constantDisplay.PolarAxes.ArcMinorTickVisibility = 0
solution3D_flux_constantDisplay.PolarAxes.DeltaAngleMajor = 10.0
solution3D_flux_constantDisplay.PolarAxes.DeltaAngleMinor = 5.0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
solution3D_flux_constantDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
solution3D_flux_constantDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
solution3D_flux_constantDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
solution3D_flux_constantDisplay.PolarAxes.ArcMajorTickSize = 0.0
solution3D_flux_constantDisplay.PolarAxes.ArcTickRatioSize = 0.3
solution3D_flux_constantDisplay.PolarAxes.ArcMajorTickThickness = 1.0
solution3D_flux_constantDisplay.PolarAxes.ArcTickRatioThickness = 0.5
solution3D_flux_constantDisplay.PolarAxes.Use2DMode = 0
solution3D_flux_constantDisplay.PolarAxes.UseLogAxis = 0

# get the material library
materialLibrary1 = GetMaterialLibrary()

# reset view to fit data
renderView1.ResetCamera(False)

# change representation type
solution3D_flux_constantDisplay.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(solution3D_flux_constantDisplay, ('POINTS', 'sol1'))

# rescale color and/or opacity maps used to include current data range
solution3D_flux_constantDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
solution3D_flux_constantDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'sol1'
sol1LUT = GetColorTransferFunction('sol1')
sol1LUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
sol1LUT.InterpretValuesAsCategories = 0
sol1LUT.AnnotationsInitialized = 0
sol1LUT.ShowCategoricalColorsinDataRangeOnly = 0
sol1LUT.RescaleOnVisibilityChange = 0
sol1LUT.EnableOpacityMapping = 0
sol1LUT.RGBPoints = [20.0, 0.231373, 0.298039, 0.752941, 20.001953125, 0.865003, 0.865003, 0.865003, 20.00390625, 0.705882, 0.0156863, 0.14902]
sol1LUT.UseLogScale = 0
sol1LUT.UseOpacityControlPointsFreehandDrawing = 0
sol1LUT.ShowDataHistogram = 0
sol1LUT.AutomaticDataHistogramComputation = 0
sol1LUT.DataHistogramNumberOfBins = 10
sol1LUT.ColorSpace = 'Diverging'
sol1LUT.UseBelowRangeColor = 0
sol1LUT.BelowRangeColor = [0.0, 0.0, 0.0]
sol1LUT.UseAboveRangeColor = 0
sol1LUT.AboveRangeColor = [0.5, 0.5, 0.5]
sol1LUT.NanColor = [1.0, 1.0, 0.0]
sol1LUT.NanOpacity = 1.0
sol1LUT.Discretize = 1
sol1LUT.NumberOfTableValues = 256
sol1LUT.ScalarRangeInitialized = 1.0
sol1LUT.HSVWrap = 0
sol1LUT.VectorComponent = 0
sol1LUT.VectorMode = 'Magnitude'
sol1LUT.AllowDuplicateScalars = 1
sol1LUT.Annotations = []
sol1LUT.ActiveAnnotatedValues = []
sol1LUT.IndexedColors = []
sol1LUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'sol1'
sol1PWF = GetOpacityTransferFunction('sol1')
sol1PWF.Points = [20.0, 0.0, 0.5, 0.0, 20.00390625, 1.0, 0.5, 0.0]
sol1PWF.AllowDuplicateScalars = 1
sol1PWF.UseLogScale = 0
sol1PWF.ScalarRangeInitialized = 1

# show data in view
solution3D_flux_constantDisplay = Show(solution3D_flux_constant, renderView1, 'StructuredGridRepresentation')

# reset view to fit data
renderView1.ResetCamera(False)

# show color bar/color legend
solution3D_flux_constantDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToLast()

# rescale color and/or opacity maps used to exactly fit the current data range
solution3D_flux_constantDisplay.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
sol1LUT.RescaleTransferFunction(19.141212359070778, 58.45220184326172)

# Rescale transfer function
sol1PWF.RescaleTransferFunction(19.141212359070778, 58.45220184326172)

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 57.09238815307617, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 57.216007232666016, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 57.33962631225586, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 58.45220184326172, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 56.22705078125, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 55.97981262207031, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 55.361717224121094, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 55.48533630371094, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 58.45220184326172, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 57.4632453918457, 0.7843137254901961, 0.2196078431372549, 0.20784313725490197, 58.45220184326172, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 58.20496368408203, 0.7843137254901961, 0.2196078431372549, 0.20784313725490197, 58.45220184326172, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

# Properties modified on sol1LUT
sol1LUT.RGBPoints = [19.141212359070778, 0.231373, 0.298039, 0.752941, 38.79670710116625, 0.865003, 0.865003, 0.865003, 58.45220184326172, 0.7843137254901961, 0.2196078431372549, 0.20784313725490197, 58.45220184326172, 0.7529411764705882, 0.1568627450980392, 0.1843137254901961, 58.45220184326172, 0.705882, 0.0156863, 0.14902]

animationScene1.GoToFirst()

# create a new 'Annotate Time Filter'
annotateTimeFilter1 = AnnotateTimeFilter(registrationName='AnnotateTimeFilter1', Input=solution3D_flux_constant)
annotateTimeFilter1.Format = 'Time: {time:f}'
annotateTimeFilter1.Shift = 0.0
annotateTimeFilter1.Scale = 1.0

# set active source
SetActiveSource(annotateTimeFilter1)

# show data in view
annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
annotateTimeFilter1Display.TextPropMode = '2D Text Widget'
annotateTimeFilter1Display.Interactivity = 1
annotateTimeFilter1Display.WindowLocation = 'Upper Left Corner'
annotateTimeFilter1Display.Position = [0.05, 0.05]
annotateTimeFilter1Display.Opacity = 1.0
annotateTimeFilter1Display.FontFamily = 'Arial'
annotateTimeFilter1Display.FontFile = ''
annotateTimeFilter1Display.Bold = 0
annotateTimeFilter1Display.Italic = 0
annotateTimeFilter1Display.Shadow = 0
annotateTimeFilter1Display.FontSize = 18
annotateTimeFilter1Display.Justification = 'Center'
annotateTimeFilter1Display.VerticalJustification = 'Center'
annotateTimeFilter1Display.ShowBorder = 'Only on hover'
annotateTimeFilter1Display.BackgroundColor = [1.0, 1.0, 1.0, 0.2]
annotateTimeFilter1Display.BorderThickness = 0.0
annotateTimeFilter1Display.CornerRadius = 0.0
annotateTimeFilter1Display.Padding = 1
annotateTimeFilter1Display.BasePosition = [0.0, 0.0, 0.0]
annotateTimeFilter1Display.TopPosition = [0.0, 1.0, 0.0]
annotateTimeFilter1Display.FlagSize = 1.0
annotateTimeFilter1Display.BillboardPosition = [0.0, 0.0, 0.0]
annotateTimeFilter1Display.DisplayOffset = [0, 0]

# get color legend/bar for sol1LUT in view renderView1
sol1LUTColorBar = GetScalarBar(sol1LUT, renderView1)

# Properties modified on sol1LUTColorBar
sol1LUTColorBar.Orientation = 'Horizontal'

# show data in view
annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1, 'TextSourceRepresentation')

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(652, 608)

sol1LUT.ApplyPreset('Rainbow Desaturated', True)

# current camera placement for renderView1
renderView1.CameraPosition = [51.80210714533175, 39.45004313873508, 120.62679303472432]
renderView1.CameraFocalPoint = [25.0, 5.0, 15.0]
renderView1.CameraViewUp = [-0.03055423653472004, 0.952528311028316, -0.3029129500687021]
renderView1.CameraParallelScale = 29.58039891549808

# save animation
print("Enregistrement de l'animation (flux constant)...")
SaveAnimation('../visualisation_graphiques/solution3D_instat_flux_constant.avi', renderView1, ImageResolution=[652, 608],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    FrameRate=10,
    FrameWindow=[0, 600], 
    # FFMPEG options
    Compression=1,
    Quality='2')
print("Enregistrement terminé")

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(652, 608)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [51.80210714533175, 39.45004313873508, 120.62679303472432]
renderView1.CameraFocalPoint = [25.0, 5.0, 15.0]
renderView1.CameraViewUp = [-0.03055423653472004, 0.952528311028316, -0.3029129500687021]
renderView1.CameraParallelScale = 29.58039891549808

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).