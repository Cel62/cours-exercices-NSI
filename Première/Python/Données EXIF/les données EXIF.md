# Les données EXIF

### Introduction

La prise de vue avec un appareil photo numérique (ou un smartphone) génère un fichier image souvent au format jpg. Ce fichier image ne contient pas seulement des informations détaillant chaque pixels de la photographie mais aussi des informations sur l'image elle-même (définition, résolution...) et sur la prise de vue (date et heure, lieu...). 

Ces données associées au fichier image d'un appareil photo s'appellent des métadonnées, et sont le plus souvent au format EXIF (EXchangeable Image file Format).

La plupart des logiciels de retouche photo permettent de lire ces métadonnées, nous n'allons pas utiliser ce type de logiciel mais nous allons plutôt écrire un petit programme Python.

**L'objectif du programme sera d'afficher le lieu de la prise de vue d'une photo sur une carte**.

### Extraire les données EXIF d'une photo

> **Activité 1**
> 
> Ouvrir le fichier donnees_exif.py qui comporte le code suivant :
> 
> ```python
> from PIL import Image
> 
> def get_exif(fichier):
>     img = Image.open(fichier)
>     exif_data = img._getexif()
>     return exif_data
> ```
> 
> Ajouter vos nom et prénom dans le début du script.
> 
> Lancer le programme, et utiliser la fonction *get_exif* avec comme argument le fichier *photo.jpg* :
> 
> ```python
> >>> get_exif('photo.jpg')
> ```
> 
> La fonction renvoie les données EXIF contenues dans le fichier *photo.jpg*.
> 
> <u>Remarque :</u> le script utilise le module Image de la bibliothèque Pillow (anciennement PIL) qui permet de manipuler des images avec Python.
> 
> Les documentations complètes sont disponibles ci-dessous :
> 
> * [Documentation Pillow (PIL Fork)](https://pillow.readthedocs.io/en/latest/)
> 
> * [Documentation Module Image](https://pillow.readthedocs.io/en/latest/reference/Image.html)

Comme vous pouvez le constater, les données EXIF extraites du fichier *photo.jpg* sont sous la forme d'un dictionnaire avec des clés sous forme de nombres. 

Pour comprendre la signification de ces nombres, consultez le site [Exiv2 - Image metadata library and tools](http://www.exiv2.org/tags.html).

> **Activité 2**
> 
> En s'aidant du site Exiv2, rechercher les clés permettant d'accéder :
> 
> * à la marque l'appareil photo utilisé
> 
> * au modèle de l'appareil photo utilisé
> 
> * au informations GPS contenues dans la photo
> 
> ```python
> # clé pour la marque : 271
> # clé pour le modèle : 272
> # clé pour les infos GPS : 34853
> ```
> 
> Dans le Shell, stocker temporairement les données EXIF renvoyées sous forme de dictionnaire par la fonction *get_exif* dans une variable nommée *exif* :
> 
> ```python
> >>> exif = get_exif('photo.jpg')
> ```
> 
> Observer le résultat obtenu.
> 
> Dans le shell, utiliser les clés demandées pour obtenir la marque, le modèle de l'appareil, et les informations GPS contenus dans le dictionnaire *exif* :
> 
> ```python
> # la marque de l'appareil photo
> >>> exif.get(271)
> 'samsung'
> 
> # le modèle de l'appareil photo
> >>> exif.get(272)
> 'SM-G935F'
> 
> # les informations GPS
> >>> exif.get(34853)
> {0: b'\x02\x02\x00\x00', 1: 'N', 2: ((38, 1), (44, 1), (37, 1)), 3: 'W', 4: ((109, 1), (29, 1), (57, 1)), 5: b'\x00', 6: (1446, 1), 7: ((0, 1), (31, 1), (56, 1)), 29: '2018:08:12'}
> ```

### Mise en forme des données EXIF

Comme vous l'avez constaté les données EXIF ou plus précisément les clés utilisées ne sont pas trés parlantes, nous allons améliorer cela en donnant un intitulé pour chacune de ces clés.

Pour cela, nous allons utiliser un autre module de la bibliothèque *Pillow* qui est le module *ExifTags*.

La documentation est disponible [ici](https://pillow.readthedocs.io/en/latest/reference/ExifTags.html), ce module correspond en fait à deux dictionnaires contenant les intitulés en anglais des différentes clés du dictionnaire contenant les données EXIF.

> **Activité 3**
> 
> Ajouter au début de votre programme le code ci-dessous afin d'importer le module ExifTags et les deux dictionnaires associés :
> 
> ```python
> from PIL.ExifTags import TAGS, GPSTAGS
> ```
> 
> Lancer votre programme.
> 
> Dans le shell, taper les instructions suivantes pour observer le contenu des dictionnaires *TAGS* et *GPSTAGS* :
> 
> ```python
> >>> TAGS
> # début du dictionnaire ici #
> {11: 'ProcessingSoftware', 254: 'NewSubfileType', 255: 'SubfileType', 256: 'ImageWidth', 257: 'ImageLength', 258: 'BitsPerSample', 259: 'Compression', 262: 'PhotometricInterpretation', 263: 'Thresholding', 264: 'CellWidth', 265: 'CellLength', 266: 'FillOrder', 269: 'DocumentName', 270: 'ImageDescription', 271: 'Make', 272: 'Model', 273: 'StripOffsets', 274: 'Orientation', 277: 'SamplesPerPixel', 278: 'RowsPerStrip', 279: 'StripByteCounts', 280: 'MinSampleValue', 281: 'MaxSampleValue', 282: 'XResolution', 283: 'YResolution', 284: 'PlanarConfiguration', 285: 'PageName', 288: 'FreeOffsets', 289: 'FreeByteCounts', 290: 'GrayResponseUnit', 291: 'GrayResponseCurve', 292: 'T4Options', 293: 'T6Options', 296: 'ResolutionUnit', 297: 'PageNumber', 301: 'TransferFunction', 305: 'Software', 306: 'DateTime', 315: 'Artist', 316: 'HostComputer', 317: 'Predictor', 318: 'WhitePoint', 319: 'PrimaryChromaticities', 320: 'ColorMap', 321: 'HalftoneHints', 322: 'TileWidth', 323: 'TileLength', 324: 'TileOffsets', 325: 'TileByteCounts', 330: 'SubIFDs', 332: 'InkSet', 333: 'InkNames', 334: 'NumberOfInks', 336: 'DotRange', 337: 'TargetPrinter', 338: 'ExtraSamples', 339: 'SampleFormat', 340: 'SMinSampleValue', 341: 'SMaxSampleValue', 342: 'TransferRange', 343: 'ClipPath', 344: 'XClipPathUnits', 345: 'YClipPathUnits', 346: 'Indexed', 347: 'JPEGTables', 351: 'OPIProxy', 512: 'JPEGProc', 513: 'JpegIFOffset', 514: 'JpegIFByteCount', 515: 'JpegRestartInterval', 517: 'JpegLosslessPredictors', 518: 'JpegPointTransforms', 519: 'JpegQTables', 520: 'JpegDCTables', 521: 'JpegACTables', 529: 'YCbCrCoefficients', 530: 'YCbCrSubSampling', 531: 'YCbCrPositioning', 532: 'ReferenceBlackWhite', 700: 'XMLPacket', 4096: 'RelatedImageFileFormat', 4097: 'RelatedImageWidth', 4098: 'RelatedImageLength', 18246: 'Rating', 18249: 'RatingPercent', 32781: 'ImageID', 33421: 'CFARepeatPatternDim', 33422: 'CFAPattern', 33423: 'BatteryLevel', 33432: 'Copyright', 33434: 'ExposureTime', 33437: 'FNumber', 33723: 'IPTCNAA', 34377: 'ImageResources', 34665: 'ExifOffset', 34675: 'InterColorProfile', 34850: 'ExposureProgram', 34852: 'SpectralSensitivity', 34853: 'GPSInfo', 34855: 'ISOSpeedRatings', 34856: 'OECF', 34857: 'Interlace', 34858: 'TimeZoneOffset', 34859: 'SelfTimerMode', 36864: 'ExifVersion', 36867: 'DateTimeOriginal', 36868: 'DateTimeDigitized', 37121: 'ComponentsConfiguration', 37122: 'CompressedBitsPerPixel', 37377: 'ShutterSpeedValue', 37378: 'ApertureValue', 37379: 'BrightnessValue', 37380: 'ExposureBiasValue', 37381: 'MaxApertureValue', 37382: 'SubjectDistance', 37383: 'MeteringMode', 37384: 'LightSource', 37385: 'Flash', 37386: 'FocalLength', 37387: 'FlashEnergy', 37388: 'SpatialFrequencyResponse', 37389: 'Noise', 37393: 'ImageNumber', 37394: 'SecurityClassification', 37395: 'ImageHistory', 37396: 'SubjectLocation', 37397: 'ExposureIndex', 37398: 'TIFF/EPStandardID', 37500: 'MakerNote', 37510: 'UserComment', 37520: 'SubsecTime', 37521: 'SubsecTimeOriginal', 37522: 'SubsecTimeDigitized', 40091: 'XPTitle', 40092: 'XPComment', 40093: 'XPAuthor', 40094: 'XPKeywords', 40095: 'XPSubject', 40960: 'FlashPixVersion', 40961: 'ColorSpace', 40962: 'ExifImageWidth', 40963: 'ExifImageHeight', 40964: 'RelatedSoundFile', 40965: 'ExifInteroperabilityOffset', 41483: 'FlashEnergy', 41484: 'SpatialFrequencyResponse', 41486: 'FocalPlaneXResolution', 41487: 'FocalPlaneYResolution', 41488: 'FocalPlaneResolutionUnit', 41492: 'SubjectLocation', 41493: 'ExposureIndex', 41495: 'SensingMethod', 41728: 'FileSource', 41729: 'SceneType', 41730: 'CFAPattern', 41985: 'CustomRendered', 41986: 'ExposureMode', 41987: 'WhiteBalance', 41988: 'DigitalZoomRatio', 41989: 'FocalLengthIn35mmFilm', 41990: 'SceneCaptureType', 41991: 'GainControl', 41992: 'Contrast', 41993: 'Saturation', 41994: 'Sharpness', 41995: 'DeviceSettingDescription', 41996: 'SubjectDistanceRange', 42016: 'ImageUniqueID', 42032: 'CameraOwnerName', 42033: 'BodySerialNumber', 42034: 'LensSpecification', 42035: 'LensMake', 42036: 'LensModel', 42037: 'LensSerialNumber', 42240: 'Gamma', 50341: 'PrintImageMatching', 50706: 'DNGVersion', 50707: 'DNGBackwardVersion', 50708: 'UniqueCameraModel', 50709: 'LocalizedCameraModel', 50710: 'CFAPlaneColor', 50711: 'CFALayout', 50712: 'LinearizationTable', 50713: 'BlackLevelRepeatDim', 50714: 'BlackLevel', 50715: 'BlackLevelDeltaH', 50716: 'BlackLevelDeltaV', 50717: 'WhiteLevel', 50718: 'DefaultScale', 50719: 'DefaultCropOrigin', 50720: 'DefaultCropSize', 50721: 'ColorMatrix1', 50722: 'ColorMatrix2', 50723: 'CameraCalibration1', 50724: 'CameraCalibration2', 50725: 'ReductionMatrix1', 50726: 'ReductionMatrix2', 50727: 'AnalogBalance', 50728: 'AsShotNeutral', 50729: 'AsShotWhiteXY', 50730: 'BaselineExposure', 50731: 'BaselineNoise', 50732: 'BaselineSharpness', 50733: 'BayerGreenSplit', 50734: 'LinearResponseLimit', 50735: 'CameraSerialNumber', 50736: 'LensInfo', 50737: 'ChromaBlurRadius', 50738: 'AntiAliasStrength', 50739: 'ShadowScale', 50740: 'DNGPrivateData', 50741: 'MakerNoteSafety', 50778: 'Cal…
> 
> >>> GPSTAGS
> # début du dictionnaire ici #
> {0: 'GPSVersionID', 1: 'GPSLatitudeRef', 2: 'GPSLatitude', 3: 'GPSLongitudeRef', 4: 'GPSLongitude', 5: 'GPSAltitudeRef', 6: 'GPSAltitude', 7: 'GPSTimeStamp', 8: 'GPSSatellites', 9: 'GPSStatus', 10: 'GPSMeasureMode', 11: 'GPSDOP', 12: 'GPSSpeedRef', 13: 'GPSSpeed', 14: 'GPSTrackRef', 15: 'GPSTrack', 16: 'GPSImgDirectionRef', 17: 'GPSImgDirection', 18: 'GPSMapDatum', 19: 'GPSDestLatitudeRef', 20: 'GPSDestLatitude', 21: 'GPSDestLongitudeRef', 22: 'GPSDestLongitude', 23: 'GPSDestBearingRef', 24: 'GPSDestBearing', 25: 'GPSDestDistanceRef', 26: 'GPSDestDistance', 27: 'GPSProcessingMethod', 28: 'GPSAreaInformation', 29: 'GPSDateStamp', 30: 'GPSDifferential', 31: 'GPSHPositioningError'}
> ```

Nous allons maintenant créer une fonction qui va générer un nouveau dictionnaire à partir des données EXIF du fichier photo (et du dictionnaire TAGS) dans lequel les clés seront des intitulés clairs (Make, Model, ...) et non plus des nombres.

> **Activité 4**
> 
> Compléter la fonction *exif_format* dans Thonny, sachant qu'il faut :
> 
> * que la fonction prenne comme seul argument *fichier* qui sera le nom du fichier photo à utiliser
> 
> * récupérer les données EXIF d'un fichier photo en utilisant la fonction *get_exif* et les placer dans une variable (par exemple : *exif_data*).
> 
> * créer un dictionnaire vide (par exemple : *exif_format*).
> 
> * pour chaque clés et valeur contenu dans *exif_data*, les copier dans le dictionnaire *exif_format* en remplaçant la clé sous forme de nombre par son intitulé.
> 
> <u>Par exemple (pour le début seulement) :</u>
> 
> ```python
> >>> exif_format('photo.jpg')
> {'ExifVersion': b'0220',
>  'ComponentsConfiguration': b'\x01\x02\x03\x00',
>  'ShutterSpeedValue': (1111, 100),
>  'DateTimeOriginal': '2018:08:11 17:32:14',
>  'DateTimeDigitized': '2018:08:11 17:32:14',...}
> ```

On peut maintenant plus facilement exploiter les données EXIF d'un fichier photo.

Mais l'objectif du programme étant de localiser le lieu de la prise de vue d'une photo, nous allons maintenant nous intéresser plus particulièrement aux informations GPS.

> **Activité 5**
> 
> Compléter la fonction get_gps dans Thonny, sachant que :
> 
> * la fonction doit prendre comme seul argument le nom du fichier photo à exploiter
> 
> * la fonction doit renvoyer un dictionnaire contenant toutes les informations GPS contenues dans les données EXIF
> 
> * la fonction doit réutiliser la fonction précédente *exif_format*
> 
> Par exemple :
> 
> ```python
> >>> get_gps('photo.jpg')
> {0: b'\x02\x02\x00\x00', 1: 'N', 2: ((38, 1), (44, 1), (37, 1))
> , 3: 'W', 4: ((109, 1), (29, 1), (57, 1)), 5: b'\x00'
> , 6: (1446, 1), 7: ((0, 1), (31, 1), (56, 1)), 29: '2018:08:12'}
> ```

Comme vous le constatez, la fonction get_gps renvoie un dictionnaire avec des clés sous forme de numéro peu lisibles. Nous allons utiliser le dictionnaire *GPSTAGS* pour améliorer la lisibilité.

> **Activité 6**
> 
> Compléter la fonction get_gps_format dans Thonny, sachant qu'il faut :
> 
> - que la fonction prenne comme argument le nom du fichier photo à utiliser
> 
> - récupérer les données EXIF d'un fichier photo en utilisant la fonction *get_gps* et les placer dans une variable (par exemple : *gps_data*).
> 
> - créer un dictionnaire vide (par exemple : *gps_format*).
> 
> - pour chaque clés et valeur contenu dans *gps_data*, les copier dans le dictionnaire *gps_format* en remplaçant la clé sous forme de nombre par son intitulé.
> 
> <u>Par exemple :</u>
> 
> ```python
> >>> get_gps_format('photo.jpg')
> {'GPSVersionID': b'\x02\x02\x00\x00',
>  'GPSLatitudeRef': 'N',
>  'GPSLatitude': ((38, 1), (44, 1), (37, 1)),
>  'GPSLongitudeRef': 'W',
>  'GPSLongitude': ((109, 1), (29, 1), (57, 1)),
>  'GPSAltitudeRef': b'\x00',
>  'GPSAltitude': (1446, 1),
>  'GPSTimeStamp': ((0, 1), (31, 1), (56, 1)),
>  'GPSDateStamp': '2018:08:12'}
> ```

### Créer une carte à partir des coordonnées GPS

La bibliothèque folium permet de générer une carte sous la forme d'une page html à partir de coordonnées GPS.

<u>Remarque :</u> nous utiliserons aussi le module *webbrowser* qui permettra d'ouvrir une page web à partir de python

La documentation est de folium est disponible [ici](https://python-visualization.github.io/folium/)

> **Activité 7**
> 
> Ajouter au début de votre programme le code ci-dessous afin d'importer la bibliothèque *folium* :
> 
> ```python
> import folium
> import webbrowser
> ```
> 
> Puis ajouter le code suivant à la fin de votre programme :
> 
> ```python
> carte = folium.Map(location = (50.720270499144, 1.6169276890077), zoom_start = 50)
> folium.Marker((50.720270499144, 1.6169276890077), icon = folium.Icon(color='green')).add_to(carte)
> carte.save('maCarte.html')
> webbrowser.open("maCarte.html")')
> ```
> 
> Lancer votre programme et observer !

Maintenant que vous avez découvert le fonctionnement de la bibliothèque folium, nous allons réaliser une fonction qui prend les coordonnées GPS d'une photo et qui génère la carte montrant le lieu de prise de vue.

Mais encore un détail, les données GPS dans les données EXIF sont des coordonnées sexagésimales (degrés, minute, seconde) et il faudra les convertir en coordonnées décimales (DD).

Pour cela, il faudra utiliser la formule : DD = degrés + (minute/60) + (seconde/3600) et tenir compte qu'il faudra ajouter un signe moins devant la longitude au format DD si nous sommes situés à l'ouest du méridien de Greenwich.²

> **Activité 8**
> 
> Compléter la fonction *affichage_carte* dans Thonny, sachant que :
> 
> * Vous pouvez commencer par couper puis coller le code utilisé pour la démonstration de *folium*
> 
> * La fonction prendra comme argument *fichier* qui correspondra au nom du fichier image à utiliser.
> 
> * La fonction réutilisera la fonction *get_gps_format* et stockera les informations dans une variable nommée *gps*.
> 
> * La fonction devra extraire les valeurs utiles et les convertir pour les rendre utilisables avec le module folium.
> 
> Le fait d'appeler la fonction affichage_carte avec comme argument le nom du fichier image devra entrainer l'affichage d'une carte avec un marqueur indiquant le lieu exacte de la prise de vue.

N'hésitez à essayer avec les autres photos fournies ou avec une photo prise avec votre smatphone (si la localisation a été activée).
