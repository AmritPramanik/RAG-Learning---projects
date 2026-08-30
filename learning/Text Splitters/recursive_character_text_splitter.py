from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Information technology general controls (ITGC) are controls that apply to all systems, components, processes, and data for a given organization or information technology (IT) environment. The objectives of ITGCs are to ensure the proper development and implementation of applications, as well as the integrity of programs, data files, and computer operations.

ITGCs may also be referred to as General Computer Controls (GCC) which are defined as: Controls, other than application controls, which relate to the environment within which computer-based application systems are developed, maintained and operated, and which are therefore applicable to all applications. The objectives of general controls are to ensure the proper development and implementation of applications, the integrity of program and data files and of computer operations. Like application controls, general controls may be either manual or programmed. Examples of general controls include the development and implementation of an IS strategy and an IS security policy, the organization of IS staff to separate conflicting duties and planning for disaster prevention and recovery process.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30
)

chunks = splitter.split_text(text)
print(type(chunks))
print(len(chunks))

for chunk in chunks :
    print(chunk,'\n')