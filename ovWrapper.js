/**
 * Including needed files for wrapping C dll
 */
var ref = require('ref-napi');
var ffi = require('ffi-napi');
var struct = require('ref-struct-napi')

/**
 * This is a C to JS version of the Folder Entry of Omniverse
 */
exports.OmniFolderEntry = struct({
  "relativePath":   'string',
  "access":         'uint', 
  "flags":          'uint',
  "size":           'uint',
  "modifiedTimeNs": 'uint',
  "createdTimeNs":  'uint', 
  "modifiedBy":     'string',
  "createdBy":      'string',
  "version":        'string',
  "hash":           'string', 
  "comment":        'string',
});

/**
 * Pointer type to the Folder Entry
 */
exports.OmniFolderEntryPtr = ref.refType(exports.OmniFolderEntry)

/**
 * The OmniverseJS class contains the basic helper functions
 */
exports.OmniverseJS = class OmniverseJS {

  #omniLibrary;

  constructor() {
    var oldPath = process.env.PATH;

    var dllPath = "D:/Projects/OmniverseCPP/OmniverseCPP/bin/Debug";
    process.env['PATH'] = `${process.env.PATH};${dllPath}`;
    
    var omniLibPath = "ovCLibraryd.dll";
    this.#omniLibrary = 
      ffi.Library(omniLibPath, 
                  {
                    'cSetLiveSync'                : ['void', ['bool']],
                    'cGetLiveSync'                : ['bool', []],
                    'cSetLogLevel'                : ['void', ['int']],
                    'cGetVersion'                 : ['string', []],
                    'cGetConnectionStatus'        : ['string', ['int']],
                    'cGetGlobalError'             : ['string', []],
                    'cGetLogString'               : ['string', []],
                    'cInitialize'                 : ['bool', ['bool', 'int']],
                    'cShutdown'                   : ['void', []],
                    'cDeleteStage'                : ['void', ['string', 'string']],
                    'cCreateStage'                : ['string', ['string', 'string']],
                    'cCheckpointFile'             : ['void', ['string', 'string']],
                    'cForceConnect'               : ['void', ['string']],
                    'cGetUsername'                : ['string', ['string']],
                    'cURLObjectExists'            : ['bool', ['string']],
                    'cIsValidURL'                 : ['bool', ['string']],
                    'cGetFile'                    : ['string', ['string', 'string']],
                    'cGetLocalFile'               : ['string', ['string']],
                    'cGetLocalFile'               : ['string', ['string']],
                    'cIsEntryFolder'              : ['bool', ['int']],
                    'cFetchFileEntry'             : [exports.OmniFolderEntry, ['int']],
                    'cFetchFolderEntries'         : ['void', ['string']],
                    'cTransferFile'               : ['void', ['string', 'string']],
                    'cDeleteFile'                 : ['void', ['string']],
                    'cDownloadMaterial'           : ['string', ['string']],
                    'cUploadMaterial'             : ['void', ['string', 'string']],
                    'cGetSessions'                : ['void', []],
                    'cGetSessionName'             : ['string', ['int']],
                    'cGetSessionListSize'         : ['int', []],
                    'cJoinSession'                : ['void', ['int']],
                    'cIsSessionNameValid'         : ['bool', ['string']],
                    'cCreateSession'              : ['bool', ['string']],
                    'cEndAndMergeSession'         : ['bool', []],
                    'cInitializeLiveSessionInfo'  : ['void', ['string']],
                    'cSetChannelURL'              : ['void', []],
                    'cSetAppName'                 : ['void', ['string']],
                    'cRegisterChannelCallback'    : ['void', []],
                    'cJoinChannel'                : ['void', []],
                    'cLeaveChannel'               : ['void', []],
                    'cStartApp'                   : ['void', ['int']],
                    'cRunApp'                     : ['void', []],
                    'cStopApp'                    : ['void', []],
                    'cPing'                       : ['int', []]
                  });
    
    console.log(this.#omniLibrary.cPing());
    
    process.env['PATH'] = oldPath;
  }

  initialize(canDoLiveSync = false, logLevel = 2) {
    if (this.#omniLibrary) {
       return this.#omniLibrary.cInitialize(canDoLiveSync, logLevel);
    } 
    return false;
  }

  getUsername(path) {
    if (this.#omniLibrary) {
      return this.#omniLibrary.cGetUsername(path);
    }
  }

  getVersion() {
    if (this.#omniLibrary) {
      return this.#omniLibrary.cGetVersion();
    }
  }

  shutdown() {
    if (this.#omniLibrary) {
      this.#omniLibrary.cShutdown();
    }
  }
}
