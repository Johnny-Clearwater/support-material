---
title: "{{ replace (replaceRE `^\d+-` "" .File.ContentBaseName) "-" " " | title }}"
issue: 0
date: {{ .Date }}
summary: ""
draft: true
---

