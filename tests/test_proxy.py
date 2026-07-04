#!/usr/bin/env python3
"""Functional tests for COTW Test Client proxy."""
import subprocess, sys, json, time

def test(name, fn):
    try:
        fn()
        print(f"  ✅ {name}")
    except AssertionError as e:
        print(f"  ❌ {name}: {e}")
    except Exception as e:
        print(f"  💥 {name}: {e}")

def main():
    BASE = "http://localhost:9000"
    
    print("=== COTW Test Client Tests ===\n")
    
    # Test 1: Proxy server is running
    test("Proxy server responds on /", lambda: (
        subprocess.run(["curl", "-sf", BASE + "/"], capture_output=True).returncode == 0
    ) or exec("raise AssertionError('Proxy not running')"))
    
    # Test 2: Index.html is served
    test("Serves index.html", lambda: (
        "COTW Test Client" in subprocess.run(
            ["curl", "-sf", BASE + "/"], capture_output=True, text=True
        ).stdout
    ) or exec("raise AssertionError('index.html not found')"))
    
    # Test 3: API proxy login
    test("API proxy GET /api/USER?action=login", lambda: (
        json.loads(subprocess.run(
            ["curl", "-sf", f"{BASE}/api/USER?action=login&deviceId=4df64994e692f5a00be2d29faefd8c7c50119a20"],
            capture_output=True, text=True
        ).stdout).get("result") == 1
    ) or exec("raise AssertionError('Login failed')"))
    
    # Test 4: API proxy returns _proxy_elapsed_ms
    resp = json.loads(subprocess.run(
        ["curl", "-sf", f"{BASE}/api/USER?action=login&deviceId=4df64994e692f5a00be2d29faefd8c7c50119a20"],
        capture_output=True, text=True
    ).stdout)
    test("Response includes _proxy_elapsed_ms", lambda: (
        "_proxy_elapsed_ms" in resp and resp["_proxy_elapsed_ms"] > 0
    ) or exec("raise AssertionError('Missing timing')"))
    
    print(f"\n=== Done ===")

if __name__ == "__main__":
    main()
