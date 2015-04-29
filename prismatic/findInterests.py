#Source: http://neo4j.com/blog/neo4j-building-topic-graph-prismatic-interest-graph-api/
#Reference: https://github.com/Prismatic/interest-graph#topic-tagging

#Find interests from text

import time
import requests
import json
import os
 
def RateLimited(maxPerSecond):
    minInterval = 1.0 / float(maxPerSecond)
    def decorate(func):
        lastTimeCalled = [0.0]
        def rateLimitedFunction(*args,**kargs):
            elapsed = time.clock() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait>0:
                time.sleep(leftToWait)
            ret = func(*args,**kargs)
            lastTimeCalled[0] = time.clock()
            return ret
        return rateLimitedFunction
    return decorate
 
@RateLimited(0.3)
def topics(title, body):
    payload = { 'title': title,
                'body': body,
                #get key from http://interest-graph.getprismatic.com/
                #add key to env variable
                'api-token': os.environ['prismatickey']} 
    r = requests.post("http://interest-graph.getprismatic.com/text/topic", data=payload)
    return r
#comments from http://github.com/llvm-project/llvm-project on 4/28
#http://github.com/llvm-project/llvm-project/commit/3277de79cc82d662a5b2edf025c41e9083c6ede9
#http://github.com/llvm-project/llvm-project/commit/370491c5de14adc7815b773e8ac6a0337986e901
#http://github.com/llvm-project/llvm-project/commit/d04a8cc8d05bf5d14cd58cca24dbf750ae5aca5b
#http://github.com/llvm-project/llvm-project/commit/b3042acbf00caed8a94be39c11514ce3d12a2a72
#http://github.com/llvm-project/llvm-project/commit/b439b3f7f51f578fde11983ad2a151e1a21ae5cb
#http://github.com/llvm-project/llvm-project/commit/f612473f836fe7a422729ff4815ac906550853f6
s = """Enable one of the tests for GCC. Summary: The "internal" name of vars is different between clang and GCC. All this change does is to 
       use a regex instead of the hardcoded internal name. Test Plan: dotest.py -C -p TestMiVar Reviewers: ki.stfu Reviewed By: ki.stfu 
       Subscribers: lldb-commits Differential Revision: http://reviews.llvm.org/D9128 Make getModRefInfo(Instruction *) not crash on certain 
       types of instructions Use a range loop. NFC.  Use dl_iterate_phdr on Android. It's available on Android/ARM starting with API 21 (L).
       remove RCPPS and RSQRTPS intrinsic instruction definitions We don't need codegen-only intrinsic instructions for the vector forms of 
       these instructions. This makes the reciprocal estimate instruction lowering identical to how we handle normal square roots: 
       (V)SQRTPS / (V)SQRTPD. No existing regression tests fail with this patch. Differential Revision: http://reviews.llvm.org/D9301
       Implemented ASTImporter support for Stmts and fixed some bugs in the ASTImporter that this exposed: - When importing functions, the body 
       (if any) was previously ignored. This patch ensures that the body is imported also. - When a function-local Decl is imported, the first 
       thing the ASTImporter does is import its context (via ImportDeclParts()). This can trigger importing the Decl again as part of the body of 
       the function (but only once, since the function's Decl has been added to ImportedDecls). This patch fixes that problem by extending 
       ImportDeclParts() to return the imported Decl if it was imported as part of importing its context, and the patch adds 
       ASTImporter::GetAlreadyImportedOrNull() to support this query. All callers of ImportDeclParts return the imported version of 
       the Decl if ImportDeclParts() returns it. - When creating functions, InnerLocStart of the source function was re-used without importing. 
       This is a straight up bug, and this patch makes ASTImporter import the InnerLocStart and use the imported version. - 
       When importing FileIDs, the ASTImporter previously always tried to re-load the file for the corresponding CacheEntry from disk. 
       This doesn't work if the CacheEntry corresponds to a named memory buffer. This patch changes the code so that if the UniqueID for 
       the cache entry is invalid (i.e., it is not a disk file) the whole entry is treated as if it were invalid, which forces an 
       in-memory copy of the buffer. Also added test cases, using the new support committed in 236011."""




r = topics("test title", s).json()
#print r
#{u'topics': [{u'topic': u'Android Development', u'score': 0.51725, u'id': 6840}, {u'topic': u'Programming', u'score': 0.51689, u'id': 3582}, {u'topic': u'Test Driven Development', u'score': 0.50312, u'id': 37705}]}

for topic in r['topics']:
    print topic['topic']
    #output -
    #Android Development
    #Programming
    #Test Driven Development
        