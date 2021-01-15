// SYNTAX TEST "Packages/Inno Setup/Inno Setup.sublime-syntax"
; Demonstrates copying 3 files and creating an icon.
// ^ source comment.line
// <- punctuation.definition.comment

#ifdef AppEnterprise
// <- meta.preprocessor punctuation.definition.keyword
//^^^^ meta.preprocessor
    #define AppName "My Program Enterprise Edition"
//  ^ meta.preprocessor punctuation.definition.keyword
//  ^^^^^^^ meta.preprocessor
//          ^^^^^^^ entity.name.variable
//                  ^ punctuation.definition.string.begin
//                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ string.quoted.double
//                                                ^ punctuation.definition.string.end
#else
    #define AppName "My Program"
#endif

// Preprocessor comment.
#define AppVersion GetVersionNumbersString(AddBackslash(SourcePath) + "MyProg.exe")
//                 ^^^^^^^^^^^^^^^^^^^^^^^ support.function
//                                        ^ punctuation.section.arguments.begin
//                                                      ^^^^^^^^^^ constant.other
//                                                                                ^ punctuation.section.arguments.end

#define GetVersionNumbers(str FileName, *MS, *LS)
//      ^^^^^^^^^^^^^^^^^ meta.function entity.name.function
//                       ^ punctuation.section.parameters.begin
//                        ^^^ storage.type
//                            ^^^^^^^^ variable.parameter
//                                    ^ punctuation.separator
//                                      ^ keyword.operator - keyword.operator.arithmetic
//                                              ^ punctuation.section.parameters.end
#define GetVersionNumbers(str FileName, *MS, *LS) \
    Local[0] = GetPackedVersion(FileName, Local[1]),
//           ^ keyword.operator.assignment
//             ^^^^^^^^^^^^^^^^ support.function
//                                      ^ punctuation.separator
//                                                 ^ keyword.operator.terminator

#unknown AddBackslash(SourcePath)

[Setup]
// <- meta.section-tag entity.name.namespace
AppName={#AppName}
// <- meta.directive keyword.other
//     ^ keyword.operator.assignment
//      ^^ keyword.other
//      ^^^^^^^^^^ meta.preprocessor
//               ^ keyword.other
AppVersion=1.5
// <- meta.directive keyword.other
//        ^ keyword.operator.assignment
//         ^^^ constant.numeric
WizardStyle=modern
DefaultDirName={autopf}\My Program
// <- meta.directive keyword.other
//            ^ keyword.operator.assignment
//             ^^^^^^^^ string.unquoted support.constant
//                     ^ string.unquoted - support.constant
//                                ^ - string
DefaultGroupName=My Program
UninstallDisplayIcon={app}\MyProg.exe
Compression=lzma2
// <- keyword.other
//          ^^^^^ constant.language
SolidCompression=yes
OutputDir=userdocs:Inno Setup Examples Output

UnknownDirective=$12af
// <- meta.directive invalid.illegal
//              ^ keyword.operator.assignment
//               ^^^^ constant.numeric.integer.hexadecimal

[Files]
// <- meta.section-tag entity.name.namespace
//^^^^^ meta.section-tag entity.name.namespace
Source: "MyProg.exe"; DestDir: "{app}"
Source: "MyProg.chm"; DestDir: "{app}"
Source: "Readme.txt"; DestDir: "{app}"; Flags: isreadme
// <- meta.parameter keyword.other
//    ^ keyword.operator.assignment
//      ^ punctuation.definition.string.begin
//      ^^^^^^^^^^^^ string.quoted
//                 ^ punctuation.definition.string.end
//                  ^ punctuation.separator - string
//                                             ^^^^^^^^ constant.language

[Icons]
Name: "{group}\My Program"; Filename: "{app}\MyProg.exe"

[Messages]
BeveledLabel=Inno Setup
WelcomeLabel2="This is%nNet line 100%%"
// <- meta.message keyword.other
//           ^ keyword.operator.assignment
//            ^^^^^^^^^^^^^^^^^^^^^^^^^ string.unquoted
//                    ^^ constant.character.escape
//                                  ^^ constant.character.escape
HelpTextNote=Foo %1, %2 look &Here
// <- meta.message keyword.other
//          ^ keyword.operator.assignment
//           ^^^^^^^^^^^^^^^^^^^^^ string.unquoted
//               ^^ constant.other.placeholder
//                   ^^ constant.other.placeholder
//                           ^ constant.other.placeholder
UnknownMessage=Foobar
// <- meta.message invalid.illegal
//            ^ keyword.operator.assignment
//             ^^^^^^ string.unquoted

[CustomMessages]
en.CustomMessage=Completed: 100%%2 done
// <- meta.language keyword.other
//^ punctuation.accessor
// ^^^^^^^^^^^^^ meta.message keyword.other
//              ^ keyword.operator.assignment
//               ^^^^^^^^^^^^^^^^^^^^^^ string.unquoted
//                             ^^ constant.character.escape

[Code]
// <- meta.section-tag entity.name.namespace

// <- source.pascal.embedded source.pascal

{ Retrieve given REG_SZ or REG_EXPAND_SZ value from registry or default otherwise. }
// <- comment.block.braces punctuation.definition.comment.pascal
//                                                                                 ^ comment.block.braces punctuation.definition.comment.pascal
function RegQueryOrDefault(const KeyName: String; const ValueName: String; var DefaultValue: String): String;
// <- storage.type.function keyword.declaration.function
//       ^ meta.function entity.name.function
//                        ^ meta.function.parameters
//                         ^ keyword.other
//                               ^ variable.parameter
//                                      ^ punctuation.separator
//                                        ^ storage.type
begin
// <- keyword.other
    Result := ExpandConstant(Format('{reg:%s,%s|%s}', [KeyName, ValueName, DefaultValue]));
//  ^ variable.language
//         ^^ keyword.operator.assignment
//            ^ support.function
//                                  ^ string.quoted.single punctuation.definition.string.begin
//                                                 ^ string.quoted.single punctuation.definition.string.end
end;
// <- keyword.other
// ^ punctuation.terminator
