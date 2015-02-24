#!/bin/sh

umask 077
(echo export SSH_AGENT_PID=$SSH_AGENT_PID) > ~/.agent
(echo export SSH_AUTH_SOCK=$SSH_AUTH_SOCK) >> ~/.agent
