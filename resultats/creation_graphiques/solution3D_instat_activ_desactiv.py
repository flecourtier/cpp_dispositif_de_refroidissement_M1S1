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
  filename+=['../fichiers_resultats/solution3D_instat_activ_desactiv/solution3D_activ_desactiv.'+str(n)+'.vtk']

# create a new 'Legacy VTK Reader'
solution3D_activ_desactiv = LegacyVTKReader(registrationName='solution3D_activ_desactiv.*', FileNames=filename)

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# set active source
SetActiveSource(solution3D_activ_desactiv)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
solution3D_activ_desactivDisplay = Show(solution3D_activ_desactiv, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
solution3D_activ_desactivDisplay.Selection = None
solution3D_activ_desactivDisplay.Representation = 'Outline'
solution3D_activ_desactivDisplay.ColorArrayName = [None, '']
solution3D_activ_desactivDisplay.LookupTable = None
solution3D_activ_desactivDisplay.MapScalars = 1
solution3D_activ_desactivDisplay.MultiComponentsMapping = 0
solution3D_activ_desactivDisplay.InterpolateScalarsBeforeMapping = 1
solution3D_activ_desactivDisplay.Opacity = 1.0
solution3D_activ_desactivDisplay.PointSize = 2.0
solution3D_activ_desactivDisplay.LineWidth = 1.0
solution3D_activ_desactivDisplay.RenderLinesAsTubes = 0
solution3D_activ_desactivDisplay.RenderPointsAsSpheres = 0
solution3D_activ_desactivDisplay.Interpolation = 'Gouraud'
solution3D_activ_desactivDisplay.Specular = 0.0
solution3D_activ_desactivDisplay.SpecularColor = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.SpecularPower = 100.0
solution3D_activ_desactivDisplay.Luminosity = 0.0
solution3D_activ_desactivDisplay.Ambient = 0.0
solution3D_activ_desactivDisplay.Diffuse = 1.0
solution3D_activ_desactivDisplay.Roughness = 0.3
solution3D_activ_desactivDisplay.Metallic = 0.0
solution3D_activ_desactivDisplay.EdgeTint = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.Anisotropy = 0.0
solution3D_activ_desactivDisplay.AnisotropyRotation = 0.0
solution3D_activ_desactivDisplay.BaseIOR = 1.5
solution3D_activ_desactivDisplay.CoatStrength = 0.0
solution3D_activ_desactivDisplay.CoatIOR = 2.0
solution3D_activ_desactivDisplay.CoatRoughness = 0.0
solution3D_activ_desactivDisplay.CoatColor = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.SelectTCoordArray = 'None'
solution3D_activ_desactivDisplay.SelectNormalArray = 'None'
solution3D_activ_desactivDisplay.SelectTangentArray = 'None'
solution3D_activ_desactivDisplay.Texture = None
solution3D_activ_desactivDisplay.RepeatTextures = 1
solution3D_activ_desactivDisplay.InterpolateTextures = 0
solution3D_activ_desactivDisplay.SeamlessU = 0
solution3D_activ_desactivDisplay.SeamlessV = 0
solution3D_activ_desactivDisplay.UseMipmapTextures = 0
solution3D_activ_desactivDisplay.ShowTexturesOnBackface = 1
solution3D_activ_desactivDisplay.BaseColorTexture = None
solution3D_activ_desactivDisplay.NormalTexture = None
solution3D_activ_desactivDisplay.NormalScale = 1.0
solution3D_activ_desactivDisplay.CoatNormalTexture = None
solution3D_activ_desactivDisplay.CoatNormalScale = 1.0
solution3D_activ_desactivDisplay.MaterialTexture = None
solution3D_activ_desactivDisplay.OcclusionStrength = 1.0
solution3D_activ_desactivDisplay.AnisotropyTexture = None
solution3D_activ_desactivDisplay.EmissiveTexture = None
solution3D_activ_desactivDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.FlipTextures = 0
solution3D_activ_desactivDisplay.BackfaceRepresentation = 'Follow Frontface'
solution3D_activ_desactivDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.BackfaceOpacity = 1.0
solution3D_activ_desactivDisplay.Position = [0.0, 0.0, 0.0]
solution3D_activ_desactivDisplay.Scale = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.Orientation = [0.0, 0.0, 0.0]
solution3D_activ_desactivDisplay.Origin = [0.0, 0.0, 0.0]
solution3D_activ_desactivDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
solution3D_activ_desactivDisplay.Pickable = 1
solution3D_activ_desactivDisplay.Triangulate = 0
solution3D_activ_desactivDisplay.UseShaderReplacements = 0
solution3D_activ_desactivDisplay.ShaderReplacements = ''
solution3D_activ_desactivDisplay.NonlinearSubdivisionLevel = 1
solution3D_activ_desactivDisplay.UseDataPartitions = 0
solution3D_activ_desactivDisplay.OSPRayUseScaleArray = 'All Approximate'
solution3D_activ_desactivDisplay.OSPRayScaleArray = 'sol1'
solution3D_activ_desactivDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
solution3D_activ_desactivDisplay.OSPRayMaterial = 'None'
solution3D_activ_desactivDisplay.BlockSelectors = ['/']
solution3D_activ_desactivDisplay.BlockColors = []
solution3D_activ_desactivDisplay.BlockOpacities = []
solution3D_activ_desactivDisplay.Orient = 0
solution3D_activ_desactivDisplay.OrientationMode = 'Direction'
solution3D_activ_desactivDisplay.SelectOrientationVectors = 'None'
solution3D_activ_desactivDisplay.Scaling = 0
solution3D_activ_desactivDisplay.ScaleMode = 'No Data Scaling Off'
solution3D_activ_desactivDisplay.ScaleFactor = 5.0
solution3D_activ_desactivDisplay.SelectScaleArray = 'None'
solution3D_activ_desactivDisplay.GlyphType = 'Arrow'
solution3D_activ_desactivDisplay.UseGlyphTable = 0
solution3D_activ_desactivDisplay.GlyphTableIndexArray = 'None'
solution3D_activ_desactivDisplay.UseCompositeGlyphTable = 0
solution3D_activ_desactivDisplay.UseGlyphCullingAndLOD = 0
solution3D_activ_desactivDisplay.LODValues = []
solution3D_activ_desactivDisplay.ColorByLODIndex = 0
solution3D_activ_desactivDisplay.GaussianRadius = 0.25
solution3D_activ_desactivDisplay.ShaderPreset = 'Sphere'
solution3D_activ_desactivDisplay.CustomTriangleScale = 3
solution3D_activ_desactivDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
solution3D_activ_desactivDisplay.Emissive = 0
solution3D_activ_desactivDisplay.ScaleByArray = 0
solution3D_activ_desactivDisplay.SetScaleArray = ['POINTS', 'sol1']
solution3D_activ_desactivDisplay.ScaleArrayComponent = ''
solution3D_activ_desactivDisplay.UseScaleFunction = 1
solution3D_activ_desactivDisplay.ScaleTransferFunction = 'PiecewiseFunction'
solution3D_activ_desactivDisplay.OpacityByArray = 0
solution3D_activ_desactivDisplay.OpacityArray = ['POINTS', 'sol1']
solution3D_activ_desactivDisplay.OpacityArrayComponent = ''
solution3D_activ_desactivDisplay.OpacityTransferFunction = 'PiecewiseFunction'
solution3D_activ_desactivDisplay.DataAxesGrid = 'GridAxesRepresentation'
solution3D_activ_desactivDisplay.SelectionCellLabelBold = 0
solution3D_activ_desactivDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
solution3D_activ_desactivDisplay.SelectionCellLabelFontFamily = 'Arial'
solution3D_activ_desactivDisplay.SelectionCellLabelFontFile = ''
solution3D_activ_desactivDisplay.SelectionCellLabelFontSize = 18
solution3D_activ_desactivDisplay.SelectionCellLabelItalic = 0
solution3D_activ_desactivDisplay.SelectionCellLabelJustification = 'Left'
solution3D_activ_desactivDisplay.SelectionCellLabelOpacity = 1.0
solution3D_activ_desactivDisplay.SelectionCellLabelShadow = 0
solution3D_activ_desactivDisplay.SelectionPointLabelBold = 0
solution3D_activ_desactivDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
solution3D_activ_desactivDisplay.SelectionPointLabelFontFamily = 'Arial'
solution3D_activ_desactivDisplay.SelectionPointLabelFontFile = ''
solution3D_activ_desactivDisplay.SelectionPointLabelFontSize = 18
solution3D_activ_desactivDisplay.SelectionPointLabelItalic = 0
solution3D_activ_desactivDisplay.SelectionPointLabelJustification = 'Left'
solution3D_activ_desactivDisplay.SelectionPointLabelOpacity = 1.0
solution3D_activ_desactivDisplay.SelectionPointLabelShadow = 0
solution3D_activ_desactivDisplay.PolarAxes = 'PolarAxesRepresentation'
solution3D_activ_desactivDisplay.ScalarOpacityFunction = None
solution3D_activ_desactivDisplay.ScalarOpacityUnitDistance = 2.398852817515995
solution3D_activ_desactivDisplay.SelectMapper = 'Projected tetra'
solution3D_activ_desactivDisplay.SamplingDimensions = [128, 128, 128]

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
solution3D_activ_desactivDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
solution3D_activ_desactivDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
solution3D_activ_desactivDisplay.GlyphType.TipResolution = 6
solution3D_activ_desactivDisplay.GlyphType.TipRadius = 0.1
solution3D_activ_desactivDisplay.GlyphType.TipLength = 0.35
solution3D_activ_desactivDisplay.GlyphType.ShaftResolution = 6
solution3D_activ_desactivDisplay.GlyphType.ShaftRadius = 0.03
solution3D_activ_desactivDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
solution3D_activ_desactivDisplay.ScaleTransferFunction.Points = [20.0, 0.0, 0.5, 0.0, 20.00390625, 1.0, 0.5, 0.0]
solution3D_activ_desactivDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
solution3D_activ_desactivDisplay.OpacityTransferFunction.Points = [20.0, 0.0, 0.5, 0.0, 20.00390625, 1.0, 0.5, 0.0]
solution3D_activ_desactivDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
solution3D_activ_desactivDisplay.DataAxesGrid.XTitle = 'X Axis'
solution3D_activ_desactivDisplay.DataAxesGrid.YTitle = 'Y Axis'
solution3D_activ_desactivDisplay.DataAxesGrid.ZTitle = 'Z Axis'
solution3D_activ_desactivDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
solution3D_activ_desactivDisplay.DataAxesGrid.XTitleFontFile = ''
solution3D_activ_desactivDisplay.DataAxesGrid.XTitleBold = 0
solution3D_activ_desactivDisplay.DataAxesGrid.XTitleItalic = 0
solution3D_activ_desactivDisplay.DataAxesGrid.XTitleFontSize = 12
solution3D_activ_desactivDisplay.DataAxesGrid.XTitleShadow = 0
solution3D_activ_desactivDisplay.DataAxesGrid.XTitleOpacity = 1.0
solution3D_activ_desactivDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
solution3D_activ_desactivDisplay.DataAxesGrid.YTitleFontFile = ''
solution3D_activ_desactivDisplay.DataAxesGrid.YTitleBold = 0
solution3D_activ_desactivDisplay.DataAxesGrid.YTitleItalic = 0
solution3D_activ_desactivDisplay.DataAxesGrid.YTitleFontSize = 12
solution3D_activ_desactivDisplay.DataAxesGrid.YTitleShadow = 0
solution3D_activ_desactivDisplay.DataAxesGrid.YTitleOpacity = 1.0
solution3D_activ_desactivDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
solution3D_activ_desactivDisplay.DataAxesGrid.ZTitleFontFile = ''
solution3D_activ_desactivDisplay.DataAxesGrid.ZTitleBold = 0
solution3D_activ_desactivDisplay.DataAxesGrid.ZTitleItalic = 0
solution3D_activ_desactivDisplay.DataAxesGrid.ZTitleFontSize = 12
solution3D_activ_desactivDisplay.DataAxesGrid.ZTitleShadow = 0
solution3D_activ_desactivDisplay.DataAxesGrid.ZTitleOpacity = 1.0
solution3D_activ_desactivDisplay.DataAxesGrid.FacesToRender = 63
solution3D_activ_desactivDisplay.DataAxesGrid.CullBackface = 0
solution3D_activ_desactivDisplay.DataAxesGrid.CullFrontface = 1
solution3D_activ_desactivDisplay.DataAxesGrid.ShowGrid = 0
solution3D_activ_desactivDisplay.DataAxesGrid.ShowEdges = 1
solution3D_activ_desactivDisplay.DataAxesGrid.ShowTicks = 1
solution3D_activ_desactivDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
solution3D_activ_desactivDisplay.DataAxesGrid.AxesToLabel = 63
solution3D_activ_desactivDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
solution3D_activ_desactivDisplay.DataAxesGrid.XLabelFontFile = ''
solution3D_activ_desactivDisplay.DataAxesGrid.XLabelBold = 0
solution3D_activ_desactivDisplay.DataAxesGrid.XLabelItalic = 0
solution3D_activ_desactivDisplay.DataAxesGrid.XLabelFontSize = 12
solution3D_activ_desactivDisplay.DataAxesGrid.XLabelShadow = 0
solution3D_activ_desactivDisplay.DataAxesGrid.XLabelOpacity = 1.0
solution3D_activ_desactivDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
solution3D_activ_desactivDisplay.DataAxesGrid.YLabelFontFile = ''
solution3D_activ_desactivDisplay.DataAxesGrid.YLabelBold = 0
solution3D_activ_desactivDisplay.DataAxesGrid.YLabelItalic = 0
solution3D_activ_desactivDisplay.DataAxesGrid.YLabelFontSize = 12
solution3D_activ_desactivDisplay.DataAxesGrid.YLabelShadow = 0
solution3D_activ_desactivDisplay.DataAxesGrid.YLabelOpacity = 1.0
solution3D_activ_desactivDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
solution3D_activ_desactivDisplay.DataAxesGrid.ZLabelFontFile = ''
solution3D_activ_desactivDisplay.DataAxesGrid.ZLabelBold = 0
solution3D_activ_desactivDisplay.DataAxesGrid.ZLabelItalic = 0
solution3D_activ_desactivDisplay.DataAxesGrid.ZLabelFontSize = 12
solution3D_activ_desactivDisplay.DataAxesGrid.ZLabelShadow = 0
solution3D_activ_desactivDisplay.DataAxesGrid.ZLabelOpacity = 1.0
solution3D_activ_desactivDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
solution3D_activ_desactivDisplay.DataAxesGrid.XAxisPrecision = 2
solution3D_activ_desactivDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
solution3D_activ_desactivDisplay.DataAxesGrid.XAxisLabels = []
solution3D_activ_desactivDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
solution3D_activ_desactivDisplay.DataAxesGrid.YAxisPrecision = 2
solution3D_activ_desactivDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
solution3D_activ_desactivDisplay.DataAxesGrid.YAxisLabels = []
solution3D_activ_desactivDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
solution3D_activ_desactivDisplay.DataAxesGrid.ZAxisPrecision = 2
solution3D_activ_desactivDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
solution3D_activ_desactivDisplay.DataAxesGrid.ZAxisLabels = []
solution3D_activ_desactivDisplay.DataAxesGrid.UseCustomBounds = 0
solution3D_activ_desactivDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
solution3D_activ_desactivDisplay.PolarAxes.Visibility = 0
solution3D_activ_desactivDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
solution3D_activ_desactivDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
solution3D_activ_desactivDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
solution3D_activ_desactivDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
solution3D_activ_desactivDisplay.PolarAxes.EnableCustomRange = 0
solution3D_activ_desactivDisplay.PolarAxes.CustomRange = [0.0, 1.0]
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisVisibility = 1
solution3D_activ_desactivDisplay.PolarAxes.RadialAxesVisibility = 1
solution3D_activ_desactivDisplay.PolarAxes.DrawRadialGridlines = 1
solution3D_activ_desactivDisplay.PolarAxes.PolarArcsVisibility = 1
solution3D_activ_desactivDisplay.PolarAxes.DrawPolarArcsGridlines = 1
solution3D_activ_desactivDisplay.PolarAxes.NumberOfRadialAxes = 0
solution3D_activ_desactivDisplay.PolarAxes.AutoSubdividePolarAxis = 1
solution3D_activ_desactivDisplay.PolarAxes.NumberOfPolarAxis = 0
solution3D_activ_desactivDisplay.PolarAxes.MinimumRadius = 0.0
solution3D_activ_desactivDisplay.PolarAxes.MinimumAngle = 0.0
solution3D_activ_desactivDisplay.PolarAxes.MaximumAngle = 90.0
solution3D_activ_desactivDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
solution3D_activ_desactivDisplay.PolarAxes.Ratio = 1.0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTitleVisibility = 1
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
solution3D_activ_desactivDisplay.PolarAxes.PolarLabelVisibility = 1
solution3D_activ_desactivDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
solution3D_activ_desactivDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
solution3D_activ_desactivDisplay.PolarAxes.RadialLabelVisibility = 1
solution3D_activ_desactivDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
solution3D_activ_desactivDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
solution3D_activ_desactivDisplay.PolarAxes.RadialUnitsVisibility = 1
solution3D_activ_desactivDisplay.PolarAxes.ScreenSize = 10.0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTitleFontFile = ''
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTitleBold = 0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTitleItalic = 0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTitleShadow = 0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTitleFontSize = 12
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisLabelFontFile = ''
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisLabelBold = 0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisLabelItalic = 0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisLabelShadow = 0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisLabelFontSize = 12
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisTextBold = 0
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisTextItalic = 0
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisTextShadow = 0
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
solution3D_activ_desactivDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
solution3D_activ_desactivDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
solution3D_activ_desactivDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
solution3D_activ_desactivDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
solution3D_activ_desactivDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
solution3D_activ_desactivDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
solution3D_activ_desactivDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
solution3D_activ_desactivDisplay.PolarAxes.EnableDistanceLOD = 1
solution3D_activ_desactivDisplay.PolarAxes.DistanceLODThreshold = 0.7
solution3D_activ_desactivDisplay.PolarAxes.EnableViewAngleLOD = 1
solution3D_activ_desactivDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
solution3D_activ_desactivDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
solution3D_activ_desactivDisplay.PolarAxes.PolarTicksVisibility = 1
solution3D_activ_desactivDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
solution3D_activ_desactivDisplay.PolarAxes.TickLocation = 'Both'
solution3D_activ_desactivDisplay.PolarAxes.AxisTickVisibility = 1
solution3D_activ_desactivDisplay.PolarAxes.AxisMinorTickVisibility = 0
solution3D_activ_desactivDisplay.PolarAxes.ArcTickVisibility = 1
solution3D_activ_desactivDisplay.PolarAxes.ArcMinorTickVisibility = 0
solution3D_activ_desactivDisplay.PolarAxes.DeltaAngleMajor = 10.0
solution3D_activ_desactivDisplay.PolarAxes.DeltaAngleMinor = 5.0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
solution3D_activ_desactivDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
solution3D_activ_desactivDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
solution3D_activ_desactivDisplay.PolarAxes.ArcMajorTickSize = 0.0
solution3D_activ_desactivDisplay.PolarAxes.ArcTickRatioSize = 0.3
solution3D_activ_desactivDisplay.PolarAxes.ArcMajorTickThickness = 1.0
solution3D_activ_desactivDisplay.PolarAxes.ArcTickRatioThickness = 0.5
solution3D_activ_desactivDisplay.PolarAxes.Use2DMode = 0
solution3D_activ_desactivDisplay.PolarAxes.UseLogAxis = 0

# get the material library
materialLibrary1 = GetMaterialLibrary()

# reset view to fit data
renderView1.ResetCamera(False)

# change representation type
solution3D_activ_desactivDisplay.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(solution3D_activ_desactivDisplay, ('POINTS', 'sol1'))

# rescale color and/or opacity maps used to include current data range
solution3D_activ_desactivDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
solution3D_activ_desactivDisplay.SetScalarBarVisibility(renderView1, True)

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
solution3D_activ_desactivDisplay = Show(solution3D_activ_desactiv, renderView1, 'StructuredGridRepresentation')

# reset view to fit data
renderView1.ResetCamera(False)

# show color bar/color legend
solution3D_activ_desactivDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToLast()

# rescale color and/or opacity maps used to exactly fit the current data range
solution3D_activ_desactivDisplay.RescaleTransferFunctionToDataRange(False, True)

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
annotateTimeFilter1 = AnnotateTimeFilter(registrationName='AnnotateTimeFilter1', Input=solution3D_activ_desactiv)
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
print("Enregistrement de l'animation (activ-desactiv)...")
SaveAnimation('../visualisation_graphiques/solution3D_instat_activ_desactiv.avi', renderView1, ImageResolution=[652, 608],
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