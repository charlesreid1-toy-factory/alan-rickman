SHELL=/bin/bash

ifeq ($(shell echo ${ALAN_RICKMAN_HOME}),)
$(error Environment variable ALAN_RICKMAN_HOME not defined. Please run "source environment" in the repo root directory before running make commands)
endif
