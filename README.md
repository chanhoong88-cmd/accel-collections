# Accel Collection — collections.accelgroup.asia

Static site for the Accel Collection residences, deployed on Vercel.

## Build

```
python3 build4.py && python3 build5.py && python3 build6.py && python3 build7.py && python3 build8.py
```

Output goes to `out/` (see `vercel.json`). `build_base.py` holds the base page generator; the numbered scripts layer content and SEO changes on top. Images live in `src/img/` and `svc/`.
