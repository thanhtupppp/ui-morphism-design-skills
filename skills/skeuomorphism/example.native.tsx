import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function SkeuomorphismNativeCard({ onPress, disabled = false }: { onPress?: () => void; disabled?: boolean }) {
  const { width } = useWindowDimensions();
  const compact = width < 600;
  return (
    <View style={[styles.card, compact && styles.cardCompact]}>
      <Text style={styles.title}>Device control</Text>
      <Text style={styles.body}>Use bounded physical cues; semantics and state stay native.</Text>
      <Pressable
        disabled={disabled}
        accessibilityRole="button"
        accessibilityState={{ disabled }}
        onPress={onPress}
        style={({ pressed }) => [styles.button, pressed && styles.pressed, disabled && styles.disabled]}
      >
        <Text style={styles.buttonLabel}>Activate</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: 20, borderRadius: 14, borderWidth: 1, borderColor: '#8a8a8a', backgroundColor: '#d8d8d8', shadowColor: '#000', shadowOpacity: 0.24, shadowRadius: 8, shadowOffset: { width: 0, height: 5 }, elevation: 5 },
  cardCompact: { padding: 16 },
  title: { fontSize: 20, fontWeight: '700' },
  body: { marginTop: 8, color: '#303030' },
  button: { marginTop: 16, minHeight: 48, paddingHorizontal: 18, justifyContent: 'center', borderRadius: 8, borderWidth: 1, borderColor: '#666', backgroundColor: '#bdbdbd' },
  pressed: { transform: [{ translateY: 1 }], shadowOpacity: 0.12, elevation: 2 },
  disabled: { opacity: 0.55 },
  buttonLabel: { textAlign: 'center', fontWeight: '700' },
});

// Verification: native Pressable semantics, compact-width adaptation, explicit pressed/disabled states, and bounded shadow.
// Fallback: remove shadow while preserving border, hierarchy, labels, and state.
