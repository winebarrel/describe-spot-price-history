describe-spot-price-history
===========================

Description
-----------

a command line tool for describing the Spot Price history.

Usage
-----
::

  shell> describe-spot-price-history -h
  Usage: describe-spot-price-history [options]
      -k, --access-key ACCESS_KEY
      -s, --secret-key SECRET_KEY
      -r, --region REGION
          --start-time TIME
          --end-time TIME
      -t, --types TYPE_LIST
      -d, --descs DESC_LIST
      -z, --zone AVAILABILITY_ZONE
          --max MAX_RESULTS
          --head N
          --tail N
          --attrs ATTR_LIST
          --sort ATTR_LIST
          --reverse
          --csv
          --tsv
      -f, --filter FILTER
  shell> export AWS_ACCESS_KEY_ID='...'
  shell> export AWS_SECRET_ACCESS_KEY='...'
  shell> export EC2_REGION=ap-northeast-1
  shell> describe-spot-price-history -r ap-northeast-1
  ---
  - [m1.small, Linux/UNIX, "0.017000", "2013-01-26T08:18:57Z", ap-northeast-1b]
  - [m1.small, Linux/UNIX, "0.020000", "2013-01-26T08:13:03Z", ap-northeast-1b]
  - [m1.small, Linux/UNIX, "0.017000", "2013-01-26T08:05:38Z", ap-northeast-1a]
  - [m1.small, Linux/UNIX, "0.020000", "2013-01-26T07:59:41Z", ap-northeast-1a]
  - [c1.xlarge, SUSE Linux, "0.202000", "2013-01-26T07:50:34Z", ap-northeast-1a]
  - [m1.medium, Windows, "0.070000", "2013-01-26T07:46:12Z", ap-northeast-1a]
  - [m1.small, Linux/UNIX, "0.017000", "2013-01-26T07:42:00Z", ap-northeast-1a]
  - [m1.small, Linux/UNIX, "0.020000", "2013-01-26T07:36:05Z", ap-northeast-1a]
  - [m1.small, Linux/UNIX, "0.017000", "2013-01-26T07:30:12Z", ap-northeast-1a]
  ...

