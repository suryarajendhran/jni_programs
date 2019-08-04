#include <stdio.h>
#include <jni.h>
#include "Sample.h"

JNIEXPORT void JNICALL Java_Sample_sayHello
  (JNIEnv *env, jobject object, jint len) {
  	printf("\nThe length of string is %d.\n\n", len);
  }