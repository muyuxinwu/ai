package main

import (
    "crypto/md5"
    "encoding/hex"
    "strings"
)

// GenerateMD5 generates MD5 hash of a string
func GenerateMD5(text string) string {
    hasher := md5.New()
    hasher.Write([]byte(text))
    return hex.EncodeToString(hasher.Sum(nil))
}

// ReverseString reverses a string
func ReverseString(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

// ContainsString checks if a string contains another string
func ContainsString(s, substr string) bool {
    return strings.Contains(s, substr)
}
