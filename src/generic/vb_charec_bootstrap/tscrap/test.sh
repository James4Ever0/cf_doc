#!/bin/bash
scrapy crawl example | grep -C 5 localhost
