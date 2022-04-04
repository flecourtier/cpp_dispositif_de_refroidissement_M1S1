# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
solution3D_statvtk = LegacyVTKReader(FileNames=['../fichiers_resultats/solution3D_stat.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [844, 544]

# show data in view
solution3D_statvtkDisplay = Show(solution3D_statvtk, renderView1)

# trace defaults for the display properties.
solution3D_statvtkDisplay.Representation = 'Outline'
solution3D_statvtkDisplay.AmbientColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.ColorArrayName = [None, '']
solution3D_statvtkDisplay.DiffuseColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.LookupTable = None
solution3D_statvtkDisplay.MapScalars = 1
solution3D_statvtkDisplay.MultiComponentsMapping = 0
solution3D_statvtkDisplay.InterpolateScalarsBeforeMapping = 1
solution3D_statvtkDisplay.Opacity = 1.0
solution3D_statvtkDisplay.PointSize = 2.0
solution3D_statvtkDisplay.LineWidth = 1.0
solution3D_statvtkDisplay.RenderLinesAsTubes = 0
solution3D_statvtkDisplay.RenderPointsAsSpheres = 0
solution3D_statvtkDisplay.Interpolation = 'Gouraud'
solution3D_statvtkDisplay.Specular = 0.0
solution3D_statvtkDisplay.SpecularColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.SpecularPower = 100.0
solution3D_statvtkDisplay.Luminosity = 0.0
solution3D_statvtkDisplay.Ambient = 0.0
solution3D_statvtkDisplay.Diffuse = 1.0
solution3D_statvtkDisplay.EdgeColor = [0.0, 0.0, 0.5]
solution3D_statvtkDisplay.BackfaceRepresentation = 'Follow Frontface'
solution3D_statvtkDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.BackfaceOpacity = 1.0
solution3D_statvtkDisplay.Position = [0.0, 0.0, 0.0]
solution3D_statvtkDisplay.Scale = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.Orientation = [0.0, 0.0, 0.0]
solution3D_statvtkDisplay.Origin = [0.0, 0.0, 0.0]
solution3D_statvtkDisplay.Pickable = 1
solution3D_statvtkDisplay.Texture = None
solution3D_statvtkDisplay.Triangulate = 0
solution3D_statvtkDisplay.UseShaderReplacements = 0
solution3D_statvtkDisplay.ShaderReplacements = ''
solution3D_statvtkDisplay.NonlinearSubdivisionLevel = 1
solution3D_statvtkDisplay.UseDataPartitions = 0
solution3D_statvtkDisplay.OSPRayUseScaleArray = 0
solution3D_statvtkDisplay.OSPRayScaleArray = 'sol1'
solution3D_statvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
solution3D_statvtkDisplay.OSPRayMaterial = 'None'
solution3D_statvtkDisplay.Orient = 0
solution3D_statvtkDisplay.OrientationMode = 'Direction'
solution3D_statvtkDisplay.SelectOrientationVectors = 'None'
solution3D_statvtkDisplay.Scaling = 0
solution3D_statvtkDisplay.ScaleMode = 'No Data Scaling Off'
solution3D_statvtkDisplay.ScaleFactor = 5.0
solution3D_statvtkDisplay.SelectScaleArray = 'None'
solution3D_statvtkDisplay.GlyphType = 'Arrow'
solution3D_statvtkDisplay.UseGlyphTable = 0
solution3D_statvtkDisplay.GlyphTableIndexArray = 'None'
solution3D_statvtkDisplay.UseCompositeGlyphTable = 0
solution3D_statvtkDisplay.UseGlyphCullingAndLOD = 0
solution3D_statvtkDisplay.LODValues = []
solution3D_statvtkDisplay.ColorByLODIndex = 0
solution3D_statvtkDisplay.GaussianRadius = 0.25
solution3D_statvtkDisplay.ShaderPreset = 'Sphere'
solution3D_statvtkDisplay.CustomTriangleScale = 3
solution3D_statvtkDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
solution3D_statvtkDisplay.Emissive = 0
solution3D_statvtkDisplay.ScaleByArray = 0
solution3D_statvtkDisplay.SetScaleArray = ['POINTS', 'sol1']
solution3D_statvtkDisplay.ScaleArrayComponent = ''
solution3D_statvtkDisplay.UseScaleFunction = 1
solution3D_statvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
solution3D_statvtkDisplay.OpacityByArray = 0
solution3D_statvtkDisplay.OpacityArray = ['POINTS', 'sol1']
solution3D_statvtkDisplay.OpacityArrayComponent = ''
solution3D_statvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
solution3D_statvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
solution3D_statvtkDisplay.SelectionCellLabelBold = 0
solution3D_statvtkDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
solution3D_statvtkDisplay.SelectionCellLabelFontFamily = 'Arial'
solution3D_statvtkDisplay.SelectionCellLabelFontFile = ''
solution3D_statvtkDisplay.SelectionCellLabelFontSize = 18
solution3D_statvtkDisplay.SelectionCellLabelItalic = 0
solution3D_statvtkDisplay.SelectionCellLabelJustification = 'Left'
solution3D_statvtkDisplay.SelectionCellLabelOpacity = 1.0
solution3D_statvtkDisplay.SelectionCellLabelShadow = 0
solution3D_statvtkDisplay.SelectionPointLabelBold = 0
solution3D_statvtkDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
solution3D_statvtkDisplay.SelectionPointLabelFontFamily = 'Arial'
solution3D_statvtkDisplay.SelectionPointLabelFontFile = ''
solution3D_statvtkDisplay.SelectionPointLabelFontSize = 18
solution3D_statvtkDisplay.SelectionPointLabelItalic = 0
solution3D_statvtkDisplay.SelectionPointLabelJustification = 'Left'
solution3D_statvtkDisplay.SelectionPointLabelOpacity = 1.0
solution3D_statvtkDisplay.SelectionPointLabelShadow = 0
solution3D_statvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
solution3D_statvtkDisplay.ScalarOpacityFunction = None
solution3D_statvtkDisplay.ScalarOpacityUnitDistance = 2.398852817515995
solution3D_statvtkDisplay.SelectMapper = 'Projected tetra'
solution3D_statvtkDisplay.SamplingDimensions = [128, 128, 128]

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
solution3D_statvtkDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
solution3D_statvtkDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
solution3D_statvtkDisplay.GlyphType.TipResolution = 6
solution3D_statvtkDisplay.GlyphType.TipRadius = 0.1
solution3D_statvtkDisplay.GlyphType.TipLength = 0.35
solution3D_statvtkDisplay.GlyphType.ShaftResolution = 6
solution3D_statvtkDisplay.GlyphType.ShaftRadius = 0.03
solution3D_statvtkDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
solution3D_statvtkDisplay.ScaleTransferFunction.Points = [44.424198150634766, 0.0, 0.5, 0.0, 58.452301025390625, 1.0, 0.5, 0.0]
solution3D_statvtkDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
solution3D_statvtkDisplay.OpacityTransferFunction.Points = [44.424198150634766, 0.0, 0.5, 0.0, 58.452301025390625, 1.0, 0.5, 0.0]
solution3D_statvtkDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
solution3D_statvtkDisplay.DataAxesGrid.XTitle = 'X Axis'
solution3D_statvtkDisplay.DataAxesGrid.YTitle = 'Y Axis'
solution3D_statvtkDisplay.DataAxesGrid.ZTitle = 'Z Axis'
solution3D_statvtkDisplay.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
solution3D_statvtkDisplay.DataAxesGrid.XTitleFontFile = ''
solution3D_statvtkDisplay.DataAxesGrid.XTitleBold = 0
solution3D_statvtkDisplay.DataAxesGrid.XTitleItalic = 0
solution3D_statvtkDisplay.DataAxesGrid.XTitleFontSize = 12
solution3D_statvtkDisplay.DataAxesGrid.XTitleShadow = 0
solution3D_statvtkDisplay.DataAxesGrid.XTitleOpacity = 1.0
solution3D_statvtkDisplay.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
solution3D_statvtkDisplay.DataAxesGrid.YTitleFontFile = ''
solution3D_statvtkDisplay.DataAxesGrid.YTitleBold = 0
solution3D_statvtkDisplay.DataAxesGrid.YTitleItalic = 0
solution3D_statvtkDisplay.DataAxesGrid.YTitleFontSize = 12
solution3D_statvtkDisplay.DataAxesGrid.YTitleShadow = 0
solution3D_statvtkDisplay.DataAxesGrid.YTitleOpacity = 1.0
solution3D_statvtkDisplay.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
solution3D_statvtkDisplay.DataAxesGrid.ZTitleFontFile = ''
solution3D_statvtkDisplay.DataAxesGrid.ZTitleBold = 0
solution3D_statvtkDisplay.DataAxesGrid.ZTitleItalic = 0
solution3D_statvtkDisplay.DataAxesGrid.ZTitleFontSize = 12
solution3D_statvtkDisplay.DataAxesGrid.ZTitleShadow = 0
solution3D_statvtkDisplay.DataAxesGrid.ZTitleOpacity = 1.0
solution3D_statvtkDisplay.DataAxesGrid.FacesToRender = 63
solution3D_statvtkDisplay.DataAxesGrid.CullBackface = 0
solution3D_statvtkDisplay.DataAxesGrid.CullFrontface = 1
solution3D_statvtkDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.DataAxesGrid.ShowGrid = 0
solution3D_statvtkDisplay.DataAxesGrid.ShowEdges = 1
solution3D_statvtkDisplay.DataAxesGrid.ShowTicks = 1
solution3D_statvtkDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
solution3D_statvtkDisplay.DataAxesGrid.AxesToLabel = 63
solution3D_statvtkDisplay.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
solution3D_statvtkDisplay.DataAxesGrid.XLabelFontFile = ''
solution3D_statvtkDisplay.DataAxesGrid.XLabelBold = 0
solution3D_statvtkDisplay.DataAxesGrid.XLabelItalic = 0
solution3D_statvtkDisplay.DataAxesGrid.XLabelFontSize = 12
solution3D_statvtkDisplay.DataAxesGrid.XLabelShadow = 0
solution3D_statvtkDisplay.DataAxesGrid.XLabelOpacity = 1.0
solution3D_statvtkDisplay.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
solution3D_statvtkDisplay.DataAxesGrid.YLabelFontFile = ''
solution3D_statvtkDisplay.DataAxesGrid.YLabelBold = 0
solution3D_statvtkDisplay.DataAxesGrid.YLabelItalic = 0
solution3D_statvtkDisplay.DataAxesGrid.YLabelFontSize = 12
solution3D_statvtkDisplay.DataAxesGrid.YLabelShadow = 0
solution3D_statvtkDisplay.DataAxesGrid.YLabelOpacity = 1.0
solution3D_statvtkDisplay.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
solution3D_statvtkDisplay.DataAxesGrid.ZLabelFontFile = ''
solution3D_statvtkDisplay.DataAxesGrid.ZLabelBold = 0
solution3D_statvtkDisplay.DataAxesGrid.ZLabelItalic = 0
solution3D_statvtkDisplay.DataAxesGrid.ZLabelFontSize = 12
solution3D_statvtkDisplay.DataAxesGrid.ZLabelShadow = 0
solution3D_statvtkDisplay.DataAxesGrid.ZLabelOpacity = 1.0
solution3D_statvtkDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
solution3D_statvtkDisplay.DataAxesGrid.XAxisPrecision = 2
solution3D_statvtkDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
solution3D_statvtkDisplay.DataAxesGrid.XAxisLabels = []
solution3D_statvtkDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
solution3D_statvtkDisplay.DataAxesGrid.YAxisPrecision = 2
solution3D_statvtkDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
solution3D_statvtkDisplay.DataAxesGrid.YAxisLabels = []
solution3D_statvtkDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
solution3D_statvtkDisplay.DataAxesGrid.ZAxisPrecision = 2
solution3D_statvtkDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
solution3D_statvtkDisplay.DataAxesGrid.ZAxisLabels = []
solution3D_statvtkDisplay.DataAxesGrid.UseCustomBounds = 0
solution3D_statvtkDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
solution3D_statvtkDisplay.PolarAxes.Visibility = 0
solution3D_statvtkDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
solution3D_statvtkDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
solution3D_statvtkDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
solution3D_statvtkDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.EnableCustomRange = 0
solution3D_statvtkDisplay.PolarAxes.CustomRange = [0.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.PolarAxisVisibility = 1
solution3D_statvtkDisplay.PolarAxes.RadialAxesVisibility = 1
solution3D_statvtkDisplay.PolarAxes.DrawRadialGridlines = 1
solution3D_statvtkDisplay.PolarAxes.PolarArcsVisibility = 1
solution3D_statvtkDisplay.PolarAxes.DrawPolarArcsGridlines = 1
solution3D_statvtkDisplay.PolarAxes.NumberOfRadialAxes = 0
solution3D_statvtkDisplay.PolarAxes.AutoSubdividePolarAxis = 1
solution3D_statvtkDisplay.PolarAxes.NumberOfPolarAxis = 0
solution3D_statvtkDisplay.PolarAxes.MinimumRadius = 0.0
solution3D_statvtkDisplay.PolarAxes.MinimumAngle = 0.0
solution3D_statvtkDisplay.PolarAxes.MaximumAngle = 90.0
solution3D_statvtkDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
solution3D_statvtkDisplay.PolarAxes.Ratio = 1.0
solution3D_statvtkDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.PolarAxisTitleVisibility = 1
solution3D_statvtkDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
solution3D_statvtkDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
solution3D_statvtkDisplay.PolarAxes.PolarLabelVisibility = 1
solution3D_statvtkDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
solution3D_statvtkDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
solution3D_statvtkDisplay.PolarAxes.RadialLabelVisibility = 1
solution3D_statvtkDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
solution3D_statvtkDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
solution3D_statvtkDisplay.PolarAxes.RadialUnitsVisibility = 1
solution3D_statvtkDisplay.PolarAxes.ScreenSize = 10.0
solution3D_statvtkDisplay.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
solution3D_statvtkDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
solution3D_statvtkDisplay.PolarAxes.PolarAxisTitleFontFile = ''
solution3D_statvtkDisplay.PolarAxes.PolarAxisTitleBold = 0
solution3D_statvtkDisplay.PolarAxes.PolarAxisTitleItalic = 0
solution3D_statvtkDisplay.PolarAxes.PolarAxisTitleShadow = 0
solution3D_statvtkDisplay.PolarAxes.PolarAxisTitleFontSize = 12
solution3D_statvtkDisplay.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
solution3D_statvtkDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
solution3D_statvtkDisplay.PolarAxes.PolarAxisLabelFontFile = ''
solution3D_statvtkDisplay.PolarAxes.PolarAxisLabelBold = 0
solution3D_statvtkDisplay.PolarAxes.PolarAxisLabelItalic = 0
solution3D_statvtkDisplay.PolarAxes.PolarAxisLabelShadow = 0
solution3D_statvtkDisplay.PolarAxes.PolarAxisLabelFontSize = 12
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisTextBold = 0
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisTextItalic = 0
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisTextShadow = 0
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
solution3D_statvtkDisplay.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
solution3D_statvtkDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
solution3D_statvtkDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
solution3D_statvtkDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
solution3D_statvtkDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
solution3D_statvtkDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
solution3D_statvtkDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
solution3D_statvtkDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
solution3D_statvtkDisplay.PolarAxes.EnableDistanceLOD = 1
solution3D_statvtkDisplay.PolarAxes.DistanceLODThreshold = 0.7
solution3D_statvtkDisplay.PolarAxes.EnableViewAngleLOD = 1
solution3D_statvtkDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
solution3D_statvtkDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
solution3D_statvtkDisplay.PolarAxes.PolarTicksVisibility = 1
solution3D_statvtkDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
solution3D_statvtkDisplay.PolarAxes.TickLocation = 'Both'
solution3D_statvtkDisplay.PolarAxes.AxisTickVisibility = 1
solution3D_statvtkDisplay.PolarAxes.AxisMinorTickVisibility = 0
solution3D_statvtkDisplay.PolarAxes.ArcTickVisibility = 1
solution3D_statvtkDisplay.PolarAxes.ArcMinorTickVisibility = 0
solution3D_statvtkDisplay.PolarAxes.DeltaAngleMajor = 10.0
solution3D_statvtkDisplay.PolarAxes.DeltaAngleMinor = 5.0
solution3D_statvtkDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
solution3D_statvtkDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
solution3D_statvtkDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
solution3D_statvtkDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
solution3D_statvtkDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
solution3D_statvtkDisplay.PolarAxes.ArcMajorTickSize = 0.0
solution3D_statvtkDisplay.PolarAxes.ArcTickRatioSize = 0.3
solution3D_statvtkDisplay.PolarAxes.ArcMajorTickThickness = 1.0
solution3D_statvtkDisplay.PolarAxes.ArcTickRatioThickness = 0.5
solution3D_statvtkDisplay.PolarAxes.Use2DMode = 0
solution3D_statvtkDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# change representation type
solution3D_statvtkDisplay.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(solution3D_statvtkDisplay, ('POINTS', 'sol1'))

# rescale color and/or opacity maps used to include current data range
solution3D_statvtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
solution3D_statvtkDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'sol1'
sol1LUT = GetColorTransferFunction('sol1')
sol1LUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
sol1LUT.InterpretValuesAsCategories = 0
sol1LUT.AnnotationsInitialized = 0
sol1LUT.ShowCategoricalColorsinDataRangeOnly = 0
sol1LUT.RescaleOnVisibilityChange = 0
sol1LUT.EnableOpacityMapping = 0
sol1LUT.RGBPoints = [44.424198150634766, 0.231373, 0.298039, 0.752941, 51.438249588012695, 0.865003, 0.865003, 0.865003, 58.452301025390625, 0.705882, 0.0156863, 0.14902]
sol1LUT.UseLogScale = 0
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

# get color legend/bar for sol1LUT in view renderView1
sol1LUTColorBar = GetScalarBar(sol1LUT, renderView1)

# Properties modified on sol1LUTColorBar
sol1LUTColorBar.AutoOrient = 0
sol1LUTColorBar.Orientation = 'Horizontal'
sol1LUTColorBar.ScalarBarThickness = 2
sol1LUTColorBar.ScalarBarLength = 0.3

# Properties modified on sol1LUTColorBar
sol1LUTColorBar.TitleFontSize = 5
sol1LUTColorBar.LabelFontSize = 5

# get opacity transfer function/opacity map for 'sol1'
sol1PWF = GetOpacityTransferFunction('sol1')
sol1PWF.Points = [44.424198150634766, 0.0, 0.5, 0.0, 58.452301025390625, 1.0, 0.5, 0.0]
sol1PWF.AllowDuplicateScalars = 1
sol1PWF.UseLogScale = 0
sol1PWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
sol1LUT.ApplyPreset('Rainbow Desaturated', True)

# current camera placement for renderView1
renderView1.CameraPosition = [51.80210714533175, 39.45004313873508, 120.62679303472432]
renderView1.CameraFocalPoint = [25.0, 5.0, 15.0]
renderView1.CameraViewUp = [-0.03055423653472004, 0.952528311028316, -0.3029129500687021]
renderView1.CameraParallelScale = 29.58039891549808

# save screenshot
SaveScreenshot('../visualisation_graphiques/solution3D_stat.png', renderView1, ImageResolution=[844, 544],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [51.80210714533175, 39.45004313873508, 120.62679303472432]
renderView1.CameraFocalPoint = [25.0, 5.0, 15.0]
renderView1.CameraViewUp = [-0.03055423653472004, 0.952528311028316, -0.3029129500687021]
renderView1.CameraParallelScale = 29.58039891549808

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).