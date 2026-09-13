import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function LiquidGlassNativeControl({ onPress }: { onPress?: () => void }) {
  const compact = useWindowDimensions().width < 600;
  return (
    <View style={[styles.shell, compact && styles.compact]}>
      <Text style={styles.title}>Context control</Text>
      <Text style={styles.body}>Use native translucent/material capabilities when available; never require blur for interaction.</Text>
      <Pressable accessibilityRole="button" accessibilityState={{ disabled: !onPress }} disabled={!onPress} onPress={onPress} style={({ pressed }) => [styles.control, pressed && styles.pressed]}>
        <Text style={styles.label}>Confirm</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  shell: { padding: 20, borderRadius: 24, borderWidth: 1, borderColor: '#aab2c5', backgroundColor: '#edf1f8' },
  compact: { padding: 16 },
  title: { fontSize: 20, fontWeight: '700' },
  body: { marginTop: 8, color: '#252a33' },
  control: { marginTop: 16, minHeight: 48, paddingHorizontal: 18, justifyContent: 'center', borderRadius: 18, borderWidth: 1, borderColor: '#77849f', backgroundColor: '#f8faff', shadowColor: '#000', shadowOpacity: 0.12, shadowRadius: 7, shadowOffset: { width: 0, height: 3 } },
  pressed: { opacity: 0.78 },
  label: { textAlign: 'center', fontWeight: '700' },
});

// Verification: bounded material, native Pressable state, compact adaptation, deterministic no-blur path.
// Fallback: opaque/static surface with the same border, hierarchy, and state model.
