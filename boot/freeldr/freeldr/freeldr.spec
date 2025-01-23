
# ARC
@ cdecl ArcClose()
@ cdecl ArcGetDiskCount()
@ cdecl ArcGetDiskInfo()
@ cdecl ArcGetFileInformation()
@ cdecl ArcGetTime()
@ cdecl ArcOpen()
@ cdecl ArcRead()
@ cdecl ArcSeek()

# Debug
@ cdecl DbgParseDebugChannels()
@ cdecl DbgPrint(str)
@ cdecl DbgPrint2(long long str long str)
@ cdecl DebugDumpBuffer()
@ cdecl DebugInit()
@ cdecl FrLdrBugCheckWithMessage()
@ stdcall KeBugCheckEx(long long long long long)

# Heap
@ cdecl FrLdrHeapAllocateEx()
@ cdecl FrLdrHeapFreeEx()
@ cdecl FrLdrHeapAlloc()
@ cdecl FrLdrHeapFree()
@ cdecl FrLdrTempAlloc()
@ cdecl FrLdrTempFree()
@ cdecl FrLdrHeapCleanupAll()

# INI (check if we can move this to rosload)
@ cdecl IniAddSection()
@ cdecl IniAddSettingValueToSection()
@ cdecl IniCleanup()
@ cdecl IniGetFileSectionListHead()
@ cdecl IniGetNumSectionItems()
@ cdecl IniGetSectionSettingNameSize()
@ cdecl IniGetSectionSettingValueSize()
@ cdecl IniFileInitialize()
@ cdecl IniModifySettingValue()
@ cdecl IniOpenSection()
@ cdecl IniReadSettingByName()
@ cdecl IniReadSettingByNumber()

# Mm
@ cdecl AddMemoryDescriptor()
@ cdecl MmAllocateHighestMemoryBelowAddress()
@ cdecl MmAllocateMemoryAtAddress()
@ cdecl MmAllocateMemoryWithType()
@ cdecl MmFreeMemory()
@ cdecl MmGetBiosMemoryMap()
@ cdecl MmGetHighestPhysicalPage()
@ cdecl MmGetLoaderPagesSpanned()
@ cdecl MmGetMemoryMap()
@ cdecl MmGetSystemMemoryMapTypeString()
@ cdecl MmGetTotalPagesInLookupTable()

# NtLdr options
@ cdecl NtLdrGetNextOption()
@ cdecl NtLdrGetOption()
@ cdecl NtLdrGetOptionEx()
@ cdecl NtLdrGetOptionExN()
@ cdecl NtLdrAddOptions()

# PeLdr
@ cdecl PeLdrAllocateDataTableEntry()
@ cdecl PeLdrCheckForLoadedDll()
@ cdecl PeLdrFreeDataTableEntry()
@ cdecl PeLdrImportDllLoadCallback()
@ cdecl PeLdrInitSecurityCookie()
@ cdecl PeLdrLoadBootImage()
@ cdecl PeLdrLoadImage()
@ cdecl PeLdrLoadImageEx()
@ cdecl PeLdrScanImportDescriptorTable()

# UI
@ cdecl UiDisplayMenu()
@ cdecl UiDrawBackdrop()
@ cdecl UiDrawProgressBarCenter()
@ cdecl UiDrawStatusText()
@ cdecl UiDrawText()
@ cdecl UiEditBox()
@ cdecl UiGetMenuBgColor()
@ cdecl UiGetScreenHeight()
@ cdecl UiIndicateProgress()
@ cdecl UiInitialize()
@ cdecl UiMessageBox()
@ cdecl UiMessageBoxCritical()
@ cdecl UiResetForSOS()
@ cdecl UiSetProgressBarSubset()
@ cdecl UiSetProgressBarText()
@ cdecl UiShowMessageBoxesInArgv()
@ cdecl UiShowMessageBoxesInSection()
@ cdecl UiUnInitialize()
@ cdecl UiUpdateProgressBar()
@ cdecl TuiPrintf()

# Other
@ cdecl ChainLoadBiosBootSectorCode()
@ cdecl ConstructArcPath()
@ cdecl DissectArcPath()
@ cdecl DiskStopFloppyMotor()
@ cdecl DriveMapGetBiosDriveNumber()
@ cdecl FrldrGetBootDrive()
@ cdecl FrldrGetBootPartition()
@ cdecl FrLdrGetBootPath()
@ cdecl FsGetServiceName()
@ cdecl FsOpenFile() # Why not ArcOpen?
@ cdecl GetArgumentValue()
@ cdecl GetBootMgrInfo()
@ cdecl IsAcpiPresent()
@ cdecl LoadSettings()
@ cdecl MachHwDetect()
@ cdecl MachPrepareForReactOS()
@ cdecl MachGetExtendedBIOSData()
@ cdecl MachVideoGetFontsFromFirmware()
@ cdecl PxeCallApi()
@ cdecl RamDiskInitialize()
@ cdecl Reboot()
@ cdecl Relocator16Boot()
@ stdcall RtlAssert(ptr ptr long ptr)
@ cdecl StallExecutionProcessor()
@ cdecl MachGetBootSectorLoadAddress()

# Additional stuff for scsiport
@ stdcall CpDoesPortExist(ptr)
@ stdcall CpEnableFifo(ptr long)
@ stdcall CpGetByte(ptr ptr long long)
@ stdcall CpInitialize(ptr ptr long)
@ stdcall CpPutByte(ptr long)
@ cdecl DissectArcPath2()
@ cdecl -i386 DriveMapMapDrivesInSection()
@ cdecl FsRegisterDevice()
@ cdecl FsGetDeviceSpecific()
@ cdecl FsSetDeviceSpecific()
@ stdcall ExAllocatePool(long long)
@ stdcall ExAllocatePoolWithTag(long long long)
@ stdcall ExFreePool(ptr)
@ stdcall ExFreePoolWithTag(ptr long)
@ cdecl MmSetMemoryType()
